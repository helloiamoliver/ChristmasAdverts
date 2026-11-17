FROM alpine:latest
RUN mkdir /var/flaskapp
WORKDIR /var/flaskapp
COPY ./code/ /var/flaskapp/
RUN apk update
RUN apk add python3 py3-pip --no-cache
CMD ["python3", "app.py"]
EXPOSE 8000
