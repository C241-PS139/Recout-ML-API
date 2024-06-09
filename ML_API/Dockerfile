FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 5000

ENV FLASK_APP=app.server:app

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]