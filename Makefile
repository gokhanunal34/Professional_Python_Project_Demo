##
## Makefile
## 
## Purpose:
## Convenience operations that may be used in a *nix environment
##

##
## Externally defined variables
##
include .env

##
## Config variables
##
SHELL=/bin/bash
SYSPY=python3.12

##
## Path variables
##
SRC_DIR=$(ROOT)/src
TEST_DIR=$(ROOT)/test

##
## Virtual Environment Variables
##
VENV=$(ROOT)/.venv
BIN=$(VENV)/bin
DEV_REQ=$(ROOT)/requirements.dev.txt
REQ=$(ROOT)/requirements.txt

###################
## Rules/recipes ##
###################

##
## Default target(s)
##
.PHONY: all
all: venv
	@echo "Creating virtual environment"

##
## Virtual environment management
##
## Automatically updates virtual environment when dependencies change
##
$(VENV): $(DEV_REQ) $(REQ)
	(\
	[[ ! -d $(VENV) ]] && $(SYSPY) -m venv $(VENV); \
	$(BIN)/pip install --upgrade pip; \
	$(BIN)/pip install -r $(DEV_REQ); \
	$(BIN)/pip install -r $(REQ); \
	touch $(VENV); \
	)

##
## Manually trigger a virtual environment build, if possible
##
.PHONY: venv
venv: $(VENV)
	@echo -e "\n\nVirtual environment configured successfully."
	@echo -e "Remember to (de)activate manually during development.\n\n"

##
## Makefile debugging
##
.PHONY: dump_vars
dump_vars:
	@echo ROOT=$(ROOT)
	@echo SRC_DIR=$(SRC_DIR)
	@echo TEST_DIR=$(TEST_DIR)
	@echo VENV=$(VENV)
	@echo BIN=$(BIN)
	@echo DEV_REQ=$(DEV_REQ)
	@echo REQ= $(REQ)
	@echo PYTHONPATH=$(PYTHONPATH)

##
## Clear cached bytecode
##
.PHONY: killcache
killcache:
	@echo -e "\nRemoving Python bytecode..."
	find $(SRC_DIR) -type f -name *.pyc -delete
	find $(TEST_DIR) -type f -name *.pyc -delete
	find $(SRC_DIR) -type d -name __pycache__ -delete
	find $(TEST_DIR) -type d -name __pycache__ -delete
	@echo -e "done.\n"

##
## Testing
##
## When pytest is invoked as `python -m pytest`, it automatically adds the current
## working directory to the PATH. This means that by setting the working directory to
## the $(SRC_DIR) directory first, we can guarantee that pytest can properly import our
## custom modules.
##
.PHONY: unit
unit: $(VENV)
	(\
	cd $(SRC_DIR); \
	export TESTING=1; \
	export PYTHONPATH=$(PYTHONPATH); \
	$(BIN)/python -m pytest $(TEST_DIR); \
	)

##
## Driver
##
## Run the provided driver program to see how the WordRank implementation performs
##
.PHONY: driver
driver: $(VENV)
	(\
	cd $(SRC_DIR); \
	$(BIN)/python driver.py; \
	)