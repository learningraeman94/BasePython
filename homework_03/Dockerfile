FROM python:3.9-buster

WORKDIR /var/app

RUN ls

COPY app/requirements.txt ./requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

COPY app .

CMD uvicorn app:app --host=0.0.0.0 --port=8000

EXPOSE 8000