FROM python:3.7-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install -U tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY preprocess.py ./preprocess.py

ENTRYPOINT [ "python", "preprocess.py"]