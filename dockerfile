FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/

RUN pip install --no-cache-dir flask gunicorn dicttoxml

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
