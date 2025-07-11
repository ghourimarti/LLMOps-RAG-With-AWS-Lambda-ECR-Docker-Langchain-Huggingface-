FROM python:3.14.0b4-slim-bookworm

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","app.py"]