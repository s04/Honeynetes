FROM tiangolo/uvicorn-gunicorn:python3.8

RUN pip install --no-cache-dir fastapi

RUN pip install pandas

COPY ./service /app

EXPOSE 80
