FROM python:3.8.6-alpine3.11
WORKDIR /service
ADD . /service
RUN pip install -r requirements.txt

CMD [ "python", "service.py"]
