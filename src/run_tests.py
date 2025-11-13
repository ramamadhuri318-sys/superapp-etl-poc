"""
Unified test runner for the SuperApp ETL project.
Runs pytest on all tests and optionally executes the ETL pipeline.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_pytest():
    """Run all pytest test files."""
    print("🧪 Running all tests with pytest...\n")
    result = subprocess.run(["pytest", "-v"], shell=True)
    if result.returncode == 0:
        print("\n✅ All tests passed successfully!")
    else:
        print("\n❌ Some tests failed.")
    return result.returncode


def run_etl():
    """Run the main ETL script after tests pass."""
    print("\n🚀 Running ETL pipeline (src/main.py)...\n")
    result = subprocess.run([sys.executable, "src/main.py"], shell=True)
    if result.returncode == 0:
        print("\n🎉 ETL script executed successfully!")
    else:
        print("\n⚠️ ETL script encountered an error.")
    return result.returncode


if __name__ == "__main__":
    # Make sure we're in project root
    os.chdir(Path(__file__).resolve().parent)

    test_code = run_pytest()
    if test_code == 0:
        run_etl()
    else:
        print("⛔ ETL skipped because tests failed.")
