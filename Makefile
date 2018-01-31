PROJECT = flask_pretty
DOCS_DIR = docs
TEST_DIR = tests

.PHONY: init develop lock dist install docs-generate docs test test-all lint readme-rst pypi-register pypi-upload pypi-test-register pypi-test-upload clean help

init:
	pipenv install --dev

develop:
	pipenv install '-e .' --dev

lock:
	pipenv lock
	pipenv lock -r > requirements.txt
	pipenv lock -r -d > requirements-dev.txt

dist:
	python setup.py sdist bdist_wheel

install:
	python setup.py install

docs-generate:
	@sphinx-quickstart

docs:
	@make -C docs html

test:
	pipenv run py.test -v --cov=$(PROJECT) --cov-report term-missing $(TEST_DIR)

test-all:
	python setup.py test

lint:
	pipenv run flake8 --ignore=F401 flask_pretty.py __about__.py tests

readme-rst:
	pandoc --from=markdown --to=rst README.md -o README.rst

pypi-register:
	python setup.py register -r pypi

pypi-upload:
	python setup.py sdist upload -r pypi

pypi-test-register:
	python setup.py register -r pypitest

pypi-test-upload:
	python setup.py sdist upload -r pypitest

clean:
	@rm -rf build dist $(DOCS_DIR)/_build $(DOCS_DIR)/_static $(DOCS_DIR)/_templates

help:
	@echo "  init               : init development environment"
	@echo "  develop            : add package as an editable dependency for local development"
	@echo "  lock               : lock the dependencies and generate requirements.txt and requirements-dev.txt"
	@echo "  dist               : create source distribution archive"
	@echo "  install            : install package"
	@echo "  docs-generate      : generate documentation from scratch (no existing index)"
	@echo "  docs               : create documentation"
	@echo "  test               : run unit tests"
	@echo "  test-all           : run the whole testing suite"
	@echo "  lint               : run the Flake8 lint checker"
	@echo "  readme-rst         : generate README.rst based on README.md"
	@echo "  pypi-register      : register current package version on PyPI (live server)"
	@echo "  pypi-upload        : upload current package version on PyPI (live server)"
	@echo "  pypi-test-register : register current package version on PyPI (test server)"
	@echo "  pypi-test-upload   : upload current package version on PyPI (test server)"
	@echo "  clean              : remove all build files"
