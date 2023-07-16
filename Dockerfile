FROM python:3.8-alpine

WORKDIR /python-docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "gunicorn", "-bind", "0.0.0.0:5000", "wsgi:app"]