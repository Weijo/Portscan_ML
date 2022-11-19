FROM ubuntu:focal

RUN apt-get update && apt-get install -y ftp curl python3 python3-pip

RUN pip install requests

COPY noise.py /

CMD ["python3", "noise.py"]