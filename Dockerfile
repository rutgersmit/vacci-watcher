FROM python:3

WORKDIR /app

RUN mkdir log

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY config.py watcher.py log.py ./

ENV TELEGRAM_CHATID=
ENV TELEGRAM_TOKEN=
ENV VACCINATION_CITY=
ENV INTERVAL=60
ENV REMOTE_SELENIUM_HOSTNAME=

LABEL maintainer="rutger.smit@gmail.com"

CMD ["watcher.py"]
