FROM python:slim

ENV PORT=8000
EXPOSE 8000
COPY ./src /app
RUN pip install mysql-connector-python

CMD [ "python", "/app/main.py" ]