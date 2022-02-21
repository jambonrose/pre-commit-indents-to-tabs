# Please type "make help" in your terminal for a list of make targets.

# ITT => Indents To Tabs
# ITT_VENV is the name of directory to store the virtual environment
ITT_VENV ?= .venv
# ITT_PYTHON is invoked to create the venv
ITT_PYTHON ?= python3

.DEFAULT_GOAL:=help

$(ITT_VENV)/bin/activate:
	mkdir -p $(ITT_VENV)
	$(ITT_PYTHON) -m venv $(ITT_VENV)
	$(ITT_VENV)/bin/pip install -r requirements-dev.txt
	$(ITT_VENV)/bin/pip install -e .

.PHONY: test ## Test the project
test: $(ITT_VENV)/bin/activate
	$(ITT_VENV)/bin/mypy src
	$(ITT_VENV)/bin/mypy tests
	$(ITT_VENV)/bin/pytest

.PHONY: tox ## Test the project in multiple Python environments
tox: $(ITT_VENV)/bin/activate
	$(ITT_VENV)/bin/tox

.PHONY: build ## Build the project for distribution
build: $(ITT_VENV)/bin/activate
	$(ITT_VENV)/bin/python3 -m build

.PHONY: clean ## Remove project development artifacts
clean:
	rm -rf dist
	rm -rf src/*.egg-info

.PHONY: purge ## Clean + remove caches, virtual environment
purge: clean
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf $(ITT_VENV)

.PHONY: help ## List make targets with description
help:
	@printf "\nUsage: make <target>\nExample: make test\n\nTargets:\n"
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) ## \(.*\)/  \1	\2/' | expand -t12
