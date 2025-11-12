# 🚀 SuperApp ETL POC

A lightweight and modular **ETL (Extract, Transform, Load)** proof-of-concept built in **Python** for dynamic JSON imports into **MongoDB**.  
Designed for quick setup, automated imports, and clean environment isolation.

---

## 📁 Project Structure

```
superapp-etl-poc/
├── src/
│   ├── main.py                 # Loads .env, triggers dynamic import
│   ├── mongo_import.py         # Core logic for MongoDB JSON import
├── tests/
│   ├── test_mongo_import.py    # Unit tests for importer
├── .env                        # Dynamic folder path & DB name configuration
├── .pre-commit-config.yaml     # Code checks & linting automation
├── .gitignore                  # Ignore venv, cache, and system files
├── dependencies.txt            # Lists required dependencies
└── README.md                   # Documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Synxa-IT-Pvt-LTD/superapp-etl-poc.git
cd superapp-etl-poc
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r dependencies.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the root:

```env
MONGO_URI=mongodb://admin:Admin%401234@<HOST>:27017/?directConnection=true
DB_NAME=superapp
DATA_PATH=./data/
```

---

## ▶️ Running the Importer

```bash
python src/main.py
```

This script:
- Loads environment variables  
- Connects to MongoDB  
- Dynamically imports JSON files from the defined path  

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🧰 Tools & Libraries

| Component | Technology |
|------------|-------------|
| Language | Python 3.10+ |
| Database | MongoDB |
| ORM/Driver | PyMongo |
| Config | python-dotenv |
| Testing | pytest |
| Code Quality | pre-commit hooks, linting |

---

## 🧠 Key Features

✅ Dynamic `.env`-based config  
✅ Automated JSON import to MongoDB  
✅ Lightweight and modular ETL design  
✅ Easy unit testing and CI integration  
✅ Cross-platform (Windows/Linux/Mac)

---

## 👥 Maintainers

**Synxa IT Pvt. Ltd.**  
📧 support@synxa.in  
🌐 [https://github.com/Synxa-IT-Pvt-LTD](https://github.com/Synxa-IT-Pvt-LTD)

---

## 🪪 License

Licensed under the **Apache License 2.0** — see the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.
