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
	mkdir -p dags logs
	docker compose up -d --build

config:
	docker compose config

preprocess-walmart:
	uv run python src/pipe/prep_data_generic.py --config config/walmart_sales.yaml

train-walmart:
	uv run python src/pipe/train_autogluon_timeseries.py --config config/walmart_sales.yaml

run-walmart: preprocess-walmart train-walmart