FROM python:latest

ENV TZ="Asia/Kolkata"

RUN date

COPY . /

RUN pip install -r requirement.txt

CMD ["python", "main.py"]