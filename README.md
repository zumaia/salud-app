# Salud-App


![](static/img/Health_Care_Professionals-ANIMATION.gif)


Este es mi proyecto final para la formación en BigData de Deusto.

Primero crear el entorno virtual
$ pipenv install flask gunicorn

Luego se acriva
$ pipenv shell

Luego instalamos los requerimientos
$ pip install -r requirements.txt

Y para ejecutar:
$ flask run
o
$ python app.py

Ahora Git
Iniciamos:
Dentro de la carpeta:
$ git init
$ git add .
$ git commit -m "Initial Commit"

Heroku:
Una vez instalado:
Nos logeamos
$ heroku login
Luego creamos la app
$ heroku creata salud-app  (es el nombre de la app)

Subimos los archivos a Heroku
$ git push heroku master

Para ver las app instaladas:
$ heroku apps
