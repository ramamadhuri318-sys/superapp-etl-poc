import os
import json
from pymongo import MongoClient


class MongoImporter:
    """
    Handles importing all JSON files from a folder into MongoDB.
    Each JSON file will be imported into a collection named after the file.
    """

    def __init__(self, mongo_uri: str, db_name: str, data_path: str):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.data_path = data_path

    def import_all(self):
        """Imports all JSON files in the folder"""
        client = MongoClient(self.mongo_uri)
        db = client[self.db_name]

        files = [f for f in os.listdir(self.data_path) if f.endswith(".json")]

        if not files:
            print("⚠️ No JSON files found in data path.")
            return

        for file in files:
            file_path = os.path.join(self.data_path, file)
            collection_name = os.path.splitext(file)[0]

            print(f"📥 Importing '{file}' → Collection: '{collection_name}'")

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if isinstance(data, dict):
                    db[collection_name].insert_one(data)
                elif isinstance(data, list) and data:
                    db[collection_name].insert_many(data)
                else:
                    print(f"⚠️ Skipped {file}: not valid JSON structure")

                print(f"✅ Successfully imported {file}")

            except Exception as e:
                print(f"❌ Error importing {file}: {e}")

        client.close()
        print("🔒 MongoDB connection closed.")
# Mongo import logic placeholder
