import os
from src.pipe.prep_data_generic import resolve_path


def test_resolve_path():
    path = "/data/01_raw/Walmart_Sales.csv"
    resolved = resolve_path(path)
    if not os.path.exists("/data"):
        assert resolved == os.path.abspath("data/01_raw/Walmart_Sales.csv")
    else:
        assert resolved == "/data/01_raw/Walmart_Sales.csv"
