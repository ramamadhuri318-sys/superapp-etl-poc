import os
import json
import pytest
import mongomock
from unittest.mock import patch
from src.mongo_import import MongoImporter


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Creates temporary JSON data for import testing."""
    folder = tmp_path / "data"
    folder.mkdir()

    file1 = folder / "employees.json"
    file1.write_text(json.dumps([
        {"name": "Alice", "role": "Analyst"},
        {"name": "Bob", "role": "Engineer"}
    ]))

    file2 = folder / "departments.json"
    file2.write_text(json.dumps([
        {"dept": "IT", "head": "Carol"},
        {"dept": "Finance", "head": "Dave"}
    ]))

    return str(folder)


def test_import_all_inserts_documents(tmp_data_dir):
    """Validates multiple JSON collections are inserted properly."""

    with patch("src.mongo_import.MongoClient", new=mongomock.MongoClient):
        importer = MongoImporter(
            mongo_uri="mongodb://fake-uri",
            db_name="test_db",
            data_path=tmp_data_dir
        )

        importer.import_all()

        client = mongomock.MongoClient()
        db = client["test_db"]

        employees = list(db["employees"].find())
        departments = list(db["departments"].find())

        assert len(employees) == 2
        assert len(departments) == 2
        assert employees[0]["name"] == "Alice"
        assert departments[1]["dept"] == "Finance"


def test_empty_folder_is_handled(tmp_path):
    """Ensures empty data folders do not cause crashes."""
    folder = tmp_path / "empty"
    folder.mkdir()

    with patch("src.mongo_import.MongoClient", new=mongomock.MongoClient):
        importer = MongoImporter("mongodb://fake", "db", str(folder))
        importer.import_all()  # Should not raise any exception

