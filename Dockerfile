FROM python:3.8-slim

WORKDIR /MLops

COPY 50_Startups.csv ./50_Startups.csv

COPY main.py ./main.py

COPY requirements.txt ./requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]