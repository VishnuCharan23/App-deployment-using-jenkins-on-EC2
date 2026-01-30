FROM python:3.9-slim
WORKDIR /app
RUN pip install Flask==2.3.3
COPY . .
CMD ["python", "app.py"]
