.PHONY: compose copy down newdb sqlite

compose:
	docker-compose build
	docker-compose up -d
	docker-compose exec main bash ||:
	docker-compose down

copy:
	docker cp sqlalchemy-skeleton_main_1:/app/main.py app/

down:
	docker-compose down

newdb:
	rm -rf pg-data

sqlite:
	docker build -t sqlalchemy-skeleton app
	docker run --rm -ti sqlalchemy-skeleton

