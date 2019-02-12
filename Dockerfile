FROM alpine:3.8

RUN apk add python3

RUN mkdir /api

COPY broadway_api /api/broadway_api
COPY requirements.txt /api
COPY api.py /api
COPY config.py /api

RUN pip3 install -r /api/requirements.txt

RUN echo "#! /bin/sh" >> /api/run.sh && \
    echo "cd /api && python3 -m src.api \"\$@\"" >> /api/run.sh && \
    chmod +x /api/run.sh && \
    ln -s /api/run.sh /usr/bin/api

CMD [ "/bin/sh" ]
