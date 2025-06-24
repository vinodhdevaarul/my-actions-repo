FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN chmod +x script.sh

RUN ls -ltra

ENTRYPOINT [ "./script.sh" ]