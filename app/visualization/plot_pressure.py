import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

RISK_COLOR = {
    "none":   None,
    "low":    "yellow",
    "medium": "orange",
    "high":   "red"
}

def make_graph(delta):
    df = delta.copy()
    df["date"] = pd.to_datetime(df["date"], utc=True)
    df["date_jst"] = df["date"].dt.tz_convert("Asia/Tokyo")
    fig, ax = plt.subplots(figsize=(10, 5))
    # plt.figure(figsize=(10, 5))
    sns.lineplot(x="date_jst", y="pressure_msl", data=df, linewidth=2, ax=ax)
    return fig, ax, df

def color_graph(ax, delta, risk_column):
    for i in range(len(delta) - 1):
        risk = delta.iloc[i][risk_column]
        color = RISK_COLOR.get(risk)
        if color is None:
            continue
        ax.axvspan(
            delta.iloc[i]["date_jst"],
            delta.iloc[i + 1]["date_jst"],
            color=color,
            alpha=0.2
        )

def show_graph(ax):
    legend_elements = [
    Patch(facecolor="red", alpha=0.3, label="High risk"),
    Patch(facecolor="orange", alpha=0.3, label="Medium risk"),
    Patch(facecolor="yellow", alpha=0.3, label="Low risk")
    ]  
    ax.set_title("Atmospheric Pressure & Sudden Change Risk (6h)")
    ax.set_xlabel("Time (JST)")
    ax.set_ylabel("Pressure (hPa)")
    ax.legend(handles=legend_elements)

# pressure_data = pd.read_csv("../storage/output.csv", parse_dates=["date"])
# sns.set_theme(style="whitegrid")
# plt.figure(figsize=(10, 5))
# sns.lineplot(x="date", y="pressure", data=pressure_data)
# plt.title("Pressure Over Time")
# plt.show()