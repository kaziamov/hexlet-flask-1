start-flask:
	set-flask-path run-flask 
set-flask-path:
	export FLASK_APP=hello
run-flask:
	flask run

start-server:
	python -m server
	