all: extract_2018 extract_2020_09_11 venv
	./venv/bin/python scripts/process.py

cache/gmd-11-369-2018-supplement.zip:
	wget -N https://doi.org/10.5194/gmd-11-369-2018-supplement -O cache/gmd-11-369-2018-supplement.zip

extract_2018: cache/gmd-11-369-2018-supplement.zip
	unzip -n -d $(basename $<) $<

cache/CEDS_v_2020_09_11_emissions.zip:
	wget -N https://zenodo.org/record/4025316/files/CEDS_v_2020_09_11_emissions.zip?download=1 \
	--directory-prefix=cache \
	--content-disposition

extract_2020_09_11: cache/CEDS_v_2020_09_11_emissions.zip
	unzip -n -d $(basename $<) $<

validate: venv
	@./venv/bin/python scripts/validate.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*/*.csv cache/*

clean-venv:
	rm -rf venv

.PHONY: clean validate
