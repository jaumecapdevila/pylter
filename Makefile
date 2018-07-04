install:
	pip install -r requirements.txt
venv:
	python3 -m venv venv
test:
	nosetests tests

.PHONY: install venv test
