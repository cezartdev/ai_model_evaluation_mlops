fmt:
	uv run ruff format .

lint:
	uv run ruff check

test:
	uv run pytest

down:
	docker compose down

rm:
	docker compose down --rmi all -v --remove-orphans

up:
	docker compose up -d --build

config:
	docker compose config