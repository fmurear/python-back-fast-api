# python-back-fast-api
Backend de python con fast api, mongodb y uvicorn.

## Server
Utilizar para lanzar **uvicorn main:app --reload --host 127.0.0.1 --port 33336** dentro de la carpeta **Backend/FastApi/**
donde main es el módulo y app es el nombre de la variable en la que iniciamos el FastAPI.

## BD
Utilizamos el comando mongodb. 
Para arrancar el servicio escribir el comando mongod.
Si nos queremos conectar a la base de datos, tenemos un plugin de vscode llamado MongoDB. Seleccionamos * *"Connect with
Connection String"* * e introducimos **mongodb//:{host}**. El host se puede buscar en la consola al haber arrancado con el comando mongod. Generalmente la conexión será algo como * *"mongodb://codespaces-2fc5a0/"* *.