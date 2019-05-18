PACKAGE := python_package_template


.PHONY: build
build:
	@make clean
	@python setup.py sdist bdist_wheel
	@twine check dist/*
	@python setup.py clean
	ls -lh dist/*

.PHONY: check
check:
	python setup.py check
	pylama

.PHONY: clean
clean:
	@rm -rf $(PACKAGE)-*.*.*/ \
		dist/ \
		pip-wheel-metadata/ \
		.eggs/ \
		.pytest_cache/ \
		.tox/ \
		*.egg-info/
	@python setup.py clean
	@find . -name "__pycache__" -type d -exec rm -rf "{}" \;
	@find . -name "*.pyc" -delete
	@find . -not -path '*/\.*' -type f | grep -E .+\.py\.[a-z0-9]{32,}\.py$ | xargs -r rm

.PHONY: fmt
fmt:
	@black $(CURDIR)
	@autoflake --in-place --recursive --remove-all-unused-imports --exclude "__init__.py" .
	@isort --apply --recursive

.PHONY: release
release:
	@python setup.py release --sign
	@make clean
