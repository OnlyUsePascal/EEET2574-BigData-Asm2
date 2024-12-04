FROM python:3.8

WORKDIR /usr/app

ADD ./requirements.txt ./

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./ ./

RUN jupyter trust ./notebook.ipynb

EXPOSE 8888

# CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

CMD ["/bin/bash", "setup.sh"]