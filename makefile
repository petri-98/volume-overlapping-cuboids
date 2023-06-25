.PHONY: clean venv test lint format

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

venv/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

venv: venv/bin/activate

test: venv/bin/activate
	coverage run -m --source=src/ --omit=*__init__.py pytest tests/
	coverage report -m

lint: venv/bin/activate
	$(PYTHON) -m pylint --recursive=y . --ignore=venv

format: venv/bin/activate
	$(PYTHON) -m yapf -ir . --exclude venv --style='{column_limit: 120}'