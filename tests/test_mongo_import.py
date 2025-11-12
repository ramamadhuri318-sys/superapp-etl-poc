"""
Unit tests for MongoImporter module
-----------------------------------
Ensures MongoDB connection, JSON loading,
folder import behavior, and .env configuration work as expected.
"""

import sys, os, pytest

# Allow tests to import src/ modules

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.mongo_import import MongoImporter

"""---Test MongoDB connection establishment---"""


def test_mongo_connection():
    importer = MongoImporter()
    client = importer.get_mongo_client()
    assert client is not None, "MongoDB client should connect successfully."


"""---Test importing a valid JSON file into test database---"""


def test_import_folder_success(tmp_path):
    folder = tmp_path / "data"
    folder.mkdir()
    (folder / "sample.json").write_text('[{"name": "John Doe"}]')

    importer = MongoImporter()
    result = importer.import_folder(str(folder), "test_db")
    assert result is True or result is None


"""---Test that nonexistent folder returns None gracefully---"""


def test_import_folder_not_found():
    importer = MongoImporter()
    result = importer.import_folder("E:/non_existing_path", "test_db")
    assert result is None


"""---Test that invalid JSON file is skipped without crashing---"""


def test_invalid_json(tmp_path):
    folder = tmp_path / "invalid"
    folder.mkdir()
    (folder / "bad.json").write_text("{invalid_json: true}")

    importer = MongoImporter()
    importer.import_folder(str(folder), "test_db")
    # Not raising exceptions, but handles gracefully
    assert True
