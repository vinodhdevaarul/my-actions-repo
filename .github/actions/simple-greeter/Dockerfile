# FROM python:3.9-slim

# WORKDIR /app

# COPY . .

# RUN chmod +x script.sh

# RUN ls -ltra

# ENTRYPOINT ["bash", "./script.sh"]

FROM python:3.14.0b3-alpine3.21

#WORKDIR /app

COPY greeter.py .

ENTRYPOINT ["python", "greeter.py"]