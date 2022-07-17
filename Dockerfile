FROM python:slim

ENV PORT=8000
EXPOSE 8000
COPY ./src /app
RUN pip install mysql-connector-python

RUN groupadd -r hellouser && useradd -r -g hellouser hellouser
USER hellouser

CMD [ "python", "/app/main.py" ]