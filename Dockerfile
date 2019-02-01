FROM alpine:3.8

RUN apk add python3

RUN mkdir /api

COPY requirements.txt /api
RUN pip3 install -r /api/requirements.txt

COPY src /api/src
COPY utils /api/utils

RUN echo "#! /bin/sh" >> /api/run.sh && \
    echo "cd /api && python3 -m src.api \"\$@\"" >> /api/run.sh && \
    chmod +x /api/run.sh && \
    ln -s /api/run.sh /usr/bin/api

CMD [ "/bin/sh" ]
