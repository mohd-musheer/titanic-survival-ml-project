FROM python:3.10-slim

WORKDIR /TITANIC

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


ENV PORT=10000

EXPOSE 10000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "10000"]

