FROM python:3.9

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install pipenv

RUN pipenv install --system --deploy --dev