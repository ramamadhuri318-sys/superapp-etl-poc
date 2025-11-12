print('Running ETL main script...')
import os
from dotenv import load_dotenv
from mongo_import import MongoImporter


def main():
    """Entry point for the ETL script"""
    load_dotenv()  # Load variables from .env file

    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")
    data_path = os.getenv("DATA_PATH")

    if not all([mongo_uri, db_name, data_path]):
        raise ValueError("❌ Missing required environment variables (MONGO_URI, DB_NAME, DATA_PATH)")

    print(f"✅ Starting import into database '{db_name}' from path '{data_path}'")

    importer = MongoImporter(mongo_uri, db_name, data_path)
    importer.import_all()

    print("🎉 ETL import completed successfully!")


if __name__ == "__main__":
    main()
