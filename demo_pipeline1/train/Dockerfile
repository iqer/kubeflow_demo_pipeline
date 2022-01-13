FROM python:3.7-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install -U tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY train.py ./train.py

ENTRYPOINT ["python", "train.py"]
