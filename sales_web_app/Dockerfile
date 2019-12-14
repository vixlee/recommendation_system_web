FROM python:3.7.0-alpine

EXPOSE 8000

COPY . /opt/web-app

WORKDIR /opt/web-app

COPY requirements.txt /opt/web-app/requirements.txt

RUN virtualenv env -p /usr/bin/python3
RUN apk add --no-cache --virtual .build-deps gcc musl-dev 
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY . .

CMD ["python3", "app.py"]