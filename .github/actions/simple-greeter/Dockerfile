# FROM python:3.9-slim

# WORKDIR /app

# COPY . .

# RUN chmod +x script.sh

# RUN ls -ltra

# ENTRYPOINT ["bash", "./script.sh"]

FROM python:3.9-slim

WORKDIR /app

COPY greeter.py .

ENTRYPOINT ["python", "greet.py"]