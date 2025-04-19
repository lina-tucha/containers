FROM python:3.9-slim

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip install flask

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]