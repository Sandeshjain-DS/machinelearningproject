FROM python:3.9-slim-buster
COPY  . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 8501
CMD [ "streamlit","run","app.py","--server.port=8501","--server.address=0.0.0.0" ]