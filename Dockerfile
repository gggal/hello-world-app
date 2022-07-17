FROM python:slim

ENV PORT=8000
EXPOSE 8000
COPY ./src /app

CMD [ "python", "/app/main.py" ]