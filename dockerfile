FROM python:3.11-slim
WORKDIR /app
RUN pip install prometheus-client
COPY memleak.py .
EXPOSE 8000
CMD ["python", "memleak.py"]
