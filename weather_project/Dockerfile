FROM python:3.11

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get clean

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
