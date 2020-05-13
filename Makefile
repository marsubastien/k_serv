
run:
	- echo Starting development server
	FLASK_APP=server.py flask run

install:
	- echo install PIP deps
	pip3 install -r requirements.txt
	python3 init_db.py