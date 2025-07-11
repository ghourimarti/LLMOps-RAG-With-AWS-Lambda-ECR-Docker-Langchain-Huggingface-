conda create -p llmops python
conda activate "D:\Coursera Courses (NVME)\LLM freecodecamp\LLMOps-sunnysavita\LLMOps-RAG-With-AWS-Lambda-ECR-Docker-Langchain-Huggingface-\llmops"


https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning


# ===============================================================
# install
curl -Ls https://astral.sh/uv/install.sh | sh
# ===============================================================
# install uv
python -m venv llmopss
source llmopss/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt

# =============================================================


# install docker
docker build -t flask-qa-app .

docker run -p 5000:5000 flask-qa-app

