from flask import Flask, request, render_template
import boto3
from langchain_aws import BedrockEmbeddings
from langchain_aws import BedrockLLM as Bedrock
from langchain_community.vectorstores import FAISS

from QASystem.ingestion import data_ingestion, get_vector_store
from QASystem.retrievalandgeneration import get_llama2_llm, get_response_llm

app = Flask(__name__)

# Initialize Bedrock client and embeddings
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        user_question = request.form.get("user_question")
        
        if request.form.get("action") == "update_vectors":
            docs = data_ingestion()
            get_vector_store(docs)
            answer = "Vector store updated successfully."
        
        elif request.form.get("action") == "run_llama":
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            llm = get_llama2_llm()
            answer = get_response_llm(llm, faiss_index, user_question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
