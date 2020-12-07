.PHONY: run build

run:
	docker run --rm -ti -v $$PWD:/app:ro sqlalchemy-skeleton

build:
	docker build -t sqlalchemy-skeleton .

