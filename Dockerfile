FROM python:alpine3.7

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pipenv

RUN pipenv install --system --deploy

CMD [ "python", "appy.py" ]