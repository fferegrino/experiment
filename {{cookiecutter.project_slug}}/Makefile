PIPENV := pipenv run

.EXPORT_ALL_VARIABLES:
EXPERIMENT_ROOT = ${PWD}
PYTHONPATH = ${PWD}/src
PIPENV_VENV_IN_PROJECT = 1

experiment:
	$(PIPENV) jupyter lab

create_env:
	pipenv install --dev

setup: create_env
