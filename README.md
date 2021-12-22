"# copecpt" 
# Prueba Técnica ApiRest Copec

## Setup

Primero clonamos el repositorio:

```sh
$ git clone https://github.com/mapizeta/copecpt.git
$ cd copecpt
```

Creamos un entorno virtual y lo activamos(Siempre recomiendo Virtualenvvwrapper para tener cada ambiente de manera ordenada https://virtualenvwrapper.readthedocs.io/en/latest/ ):

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Instalamos las dependencias:
```sh
(env)$ pip install -r requirements.txt
```

Creamos la estructura de nuestro modelo en la base de datos de prueba(sqlite)

```sh
python manage.py makemigrations api
python manage.py migrate
```

Una vez `pip` ha finalizado procedemos a arrancar nuestra api-rest:

```sh
(env)$ python manage.py runserver
```

## ENDPOINTS

`localhost:8000/user/create`

Primer punto de entrada para la creación de un usuario

`localhost:8000/user/detail`

Listado de todos los usuarios creados

`localhost:8000/user/detail/(uuid)`

Detalle de usuario por `uuid`

`localhost:8000/user/update/(uuid)/`

Actualización de usuario por `uuid`

`localhost:8000/user/delete/(uuid)/`

Eliminación de usuario por `uuid`

#Notas

- Al levantar el ambiente se creará una base de datos demo en sqlite para hacer más cómodo el trabajo con el `CRUD`
- En el repositorio se comparte un `json`(copecpt.postman_collection.json)  con los endpoint para `postman`. El uuid `4b7855b9-2a98-4acb-8c65-c7fa21db1a61` está a modo de ejemplo.