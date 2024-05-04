lint:
	flake8 .
	isort --check .
	black --check .
format:
	isort .
	black .
