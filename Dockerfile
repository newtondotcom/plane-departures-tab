FROM python:3.8-alpine

WORKDIR /python-docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "wsgi:app", "--bind", "0.0.0.0:8000"]