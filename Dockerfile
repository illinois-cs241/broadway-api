FROM alpine:3.8

RUN apk add python3

RUN mkdir /api

COPY broadway_api /api/broadway_api
COPY requirements.txt /api
COPY api.py /api
COPY config.py /api

RUN pip3 install -r /api/requirements.txt

ENTRYPOINT [ "python3", "-m", "api" ]
