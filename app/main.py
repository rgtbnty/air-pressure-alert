from api.open_meteo_client import fetch_pressure_data, export_file
from pathlib import Path
from logic.pressure_change import add_pressure_delta, calc_risk_from_delta_pressure
import pandas as pd
from logic.risk_config import RISK_CONFIG

BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"

HOUR = {
    "3h": 3,
    "6h": 6,
    "12h": 12
}

def main():
    print("GitHub Actions is running!")
    # df = fetch_pressure_data()

    # for debug
    df = pd.read_csv(STORAGE_DIR / "output.csv")
    # print(df)

    # export_file(df, STORAGE_DIR)
    delta_pressure = add_pressure_delta(df, HOUR)
    for label in ["3h", "6h", "12h"]:
        dp_col = f"dp_{label}"
        risk_col = f"risk_{label}"
        df[risk_col] = df[dp_col].apply(
            lambda dp: calc_risk_from_delta_pressure(
                dp,
                RISK_CONFIG[label]
            )
        )    
    # for debug
    # print(RISK_CONFIG)
    # print(delta_pressure)


if __name__ == "__main__":
    main()