FROM python:3.8

WORKDIR /usr/app

ADD ./requirements.txt ./

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./ ./

CMD python3 -u mongoUpload.py
