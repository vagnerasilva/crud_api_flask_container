FROM vagnerasilva/flaskgcp:1.1

#MAINTANER Your Name "youremail@domain.tld"

#RUN apt-get update -y && \
 #   apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt
COPY . /app

WORKDIR /app

#RUN pip install -r requirements.txt

EXPOSE 5000
EXPOSE 8080

#ENTRYPOINT [ "python3" ]

#CMD [ "app.py" ]

#CMD ["app.py"]
#comentar em caso de imagem para dev
CMD [ "python3", "./app.py" ]