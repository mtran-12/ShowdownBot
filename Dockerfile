FROM python:3

# RUN apt-get update && apt-get install -y python3.6 python3-pip

WORKDIR /ShowdownBot

COPY requirements.txt /ShowdownBot/requirements.txt

RUN pip3 install -r requirements.txt

COPY environment.py /ShowdownBot/environment.py

COPY run.py /ShowdownBot/run.py

COPY IOProcesses /ShowdownBot/IOProcesses

ENV PYTHONIOENCODING=utf-8

CMD ["python3", "run.py"]