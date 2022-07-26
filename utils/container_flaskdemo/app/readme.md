# Executar em modo dev
python app.py

- Sera visto algo assim

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 519-937-414

# obs: usando wsl2 o ip é diferente 


# build container do flask 1

docker build -t flaskdemo:1.0 .

# executar docker 


# montando aplicacao para desenvolvimento
docker run -it -p "8080:8080" -p 5000:5000 flaskdemo:1.0 /bin/bash

# montando aplicação para deploy
docker run -it -p "8080:8080" -p 5000:5000 flaskdemo:1.0 python ./app.py

# criando container com aplicacao rodando
docker commit 42507827adf1 vagnerasilva/flaskapp:1.0

# executando imagem preparada com portas abertas
docker run -d -p "8080:8080" -p 5000:5000 vagnerasilva/flaskapp:1.0


# Testando com ping

ping -V

ping google.com

ping http://127.0.0.1:5000


# testando com wget o python flask

wget --delete-after 0.0.0.0:5000

# Voce vera algo assim
--2022-07-25 22:36:19--  http://0.0.0.0:5000/
Connecting to 0.0.0.0:5000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 60 [application/json]
Saving to: ‘index.html.tmp’

index.html.tmp                     100%[==============================================================>]      60  --.-KB/s    in 0s       

2022-07-25 22:36:19 (3.18 MB/s) - ‘index.html.tmp’ saved [60/60]

Removing index.html.tmp.
wget --spider -S 0.0.0.0:5000
# Voce vera algo assim

Spider mode enabled. Check if remote file exists.
--2022-07-25 22:34:56--  http://0.0.0.0:5000/
Connecting to 0.0.0.0:5000... connected.
HTTP request sent, awaiting response...
  HTTP/1.1 200 OK
  Server: Werkzeug/2.2.0 Python/3.9.13
  Date: Tue, 26 Jul 2022 01:34:56 GMT
  Content-Type: application/json
  Content-Length: 60
  Connection: close
Length: 60 [application/json]
Remote file exists.