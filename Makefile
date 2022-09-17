start-flask:
	export FLASK_APP=hello
	flask run
start-server:
	poetry run server
	