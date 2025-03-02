PYTHON_VERSION=3.10
ENV_NAME=signlangvenv

.PHONY: all create-env install run clean

all: create-env install run

create-env:
	conda create -n $(ENV_NAME) python=$(PYTHON_VERSION) -y

install:
	conda activate $(ENV_NAME) && pip install -r requirements.txt

run:
	conda activate $(ENV_NAME) && python app.py

clean:
	conda remove -n $(ENV_NAME) --all -y