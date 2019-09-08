PIPENV=PIPENV_VENV_IN_PROJECT=1 pipenv
RUN_IN_PIPENV=$(PIPENV) run
SOURCES_FOLDER=./send_to_kindle
SOURCE_FILES=$(shell find . -name '*.py' -not -path **/.venv/*)
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
HASH := $(shell git rev-parse HEAD)
TAG := $(shell git tag -l --contains HEAD)


check_on_master:
ifeq ($(BRANCH),master)
	echo "You are good to go!"
else
	$(error You are not in the master branch)
endif


experiment:
	EXPERIMENT_ROOT=${PWD} \
	PYTHONPATH=${PWD}/src:${PYTHONPATH} \
	$(RUN_IN_PIPENV) jupyter lab


env:
	$(PIPENV) install --dev


patch: check_on_master
	pipenv run bumpversion patch --verbose
	git push --follow-tags

minor: check_on_master
	pipenv run bumpversion minor --verbose
	git push --follow-tags

major: check_on_master
	pipenv run bumpversion major --verbose
	git push --follow-tags
