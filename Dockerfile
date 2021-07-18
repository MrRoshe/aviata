FROM python:3.8
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install -y gcc g++ python3-dev
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt --default-timeout=100
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
