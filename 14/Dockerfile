FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY process.py .

CMD ["python3", "process.py"]