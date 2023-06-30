FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    libffi-dev \
    libnacl-dev \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY main.py ./
COPY config.py ./
COPY discordchatbot.py ./
COPY text_utils.py ./
# COPY .env ./
COPY cogs/ ./cogs/
COPY databaces/ ./databaces/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]