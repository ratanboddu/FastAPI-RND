.PHONY: clean pip

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -delete
	rm -rf *.egg-info

pip:
	pip install -e .

run:
	python main.py

