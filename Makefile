
run:
	- echo Starting development server
	FLASK_APP=server.py flask run

install:
	- echo install PIP deps
	pip3 install -r requirements.txt
	Py -3 init_db.py

pytest:
	- echo testing with PyTest
	Py -3 -m pytest