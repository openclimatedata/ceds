import json

from goodtables import validate
from goodtables.cli import _print_report
from pathlib import Path

root = Path(__file__).parents[1]

metadata = json.load(open(root / "datapackage.json", "r"))

paths = {i["name"]: i["path"] for i in metadata["resources"] if "schema" in i}
schemas = {i["name"]: i["schema"] for i in metadata["resources"] if "schema" in i}

for name, path in paths.items():
    report = validate(
        root / path,
        schema=schemas[name],
        table_limit=20,
        row_limit=600000
    )
    _print_report(report)
