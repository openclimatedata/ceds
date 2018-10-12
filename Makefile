all: extract venv
	./venv/bin/python scripts/process.py

extract: cache/gmd-11-369-2018-supplement
	unzip -n -d cache $<

cache/gmd-11-369-2018-supplement:
	wget -N https://doi.org/10.5194/gmd-11-369-2018-supplement --directory-prefix=cache

validate: venv
	@./venv/bin/python scripts/validate.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv cache/*

clean-venv:
	rm -rf venv

.PHONY: clean validate
