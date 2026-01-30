from api.open_meteo_client import fetch_pressure_data, export_file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"

def main():
    print("GitHub Actions is running!")
    df = fetch_pressure_data()
    export_file(df, STORAGE_DIR)

if __name__ == "__main__":
    main()