FROM python:3.9

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y sudo

RUN echo "### Versão do python ###"
RUN python --version
RUN pip install -r requirements.txt

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY app /app

WORKDIR /app


EXPOSE 5000
EXPOSE 8080




RUN echo "### TEstando ###"
RUN echo "### Finish Build ###"

#RUN python ./app.py
#CMD [ "python", "./app.py"]
#comentar em caso de imagem para dev
#CMD [ "python3", "./app.py" ]
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]