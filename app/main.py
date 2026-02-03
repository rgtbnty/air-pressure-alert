from api.open_meteo_client import fetch_pressure_data, export_file
from pathlib import Path
from logic.pressure_change import add_pressure_delta_inplace, calc_risk_from_delta_pressure
import pandas as pd
from logic.risk_config import RISK_CONFIG
from visualization.plot_pressure import make_graph, color_graph, show_graph, plot_risk_markers
import matplotlib.pyplot as plt

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
    add_pressure_delta_inplace(df, HOUR)
    # for label in HOUR:
    #     dp_col = f"dp_{label}"
    #     risk_col = f"risk_{label}"
    #     df[risk_col] = df[dp_col].apply(
    #         lambda dp: calc_risk_from_delta_pressure(
    #             dp,
    #             RISK_CONFIG[label]
    #         )
    #     )    
    for label in HOUR.keys():
        df[f"risk_{label}"] = df.apply(
            lambda row: calc_risk_from_delta_pressure(
                row[f"dp_diff_{label}"],
                row[f"dp_range_{label}"],
                RISK_CONFIG[label],
            ),
            axis=1,
        )

    fig, ax, df = make_graph(df)
    for label in ["3h", "6h", "12h"]:
        risk_col = f"risk_{label}"
        color_graph(ax, df, f"risk_{label}")
        plot_risk_markers(ax, df, risk_col)
    show_graph(ax, label)
    plt.tight_layout()
    plt.show()

    # for debug
    # print(RISK_CONFIG)
    # print(delta_pressure)
    # print(df["date"].dtype)
    # print(df["date"].head())


if __name__ == "__main__":
    main()