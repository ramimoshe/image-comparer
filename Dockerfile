FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
ENV PORT=80 \
    WORKER_COUNT=4

CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:80", "--workers", "4", "--worker-class", "aiohttp.worker.GunicornWebWorker"]
