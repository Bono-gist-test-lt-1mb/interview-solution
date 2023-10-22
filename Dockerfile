FROM python:3.9.6

RUN pip install requests==2.29.0 flask==3.0.0 \
    && mkdir /code 

WORKDIR /code

COPY gist_api.py tests.py .
EXPOSE 8080
CMD [ "/usr/local/bin/python", "gist_api.py" ]
