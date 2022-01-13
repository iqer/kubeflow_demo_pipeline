FROM python:3.7-slim
ADD demo.py .
RUN pip install --upgrade pip && pip install -U requests
ENTRYPOINT ["python", "demo.py"]