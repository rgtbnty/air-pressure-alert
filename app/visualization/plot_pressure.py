import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

RISK_COLOR = {
    "none":   None,
    "low":    "#4FC3F7",
    "medium": "#FFB74D",
    "high":   "#EF5350"
}

RISK_MARKER = {
    "low": ".",     
    "medium": "^",  
    "high": "X",    
}

RISK_ZORDER = {
    "none": 5,
    "low": 6,
    "medium": 7,
    "high": 8
}

def make_graph(delta):
    sns.set_theme(
    style="dark",
    rc={
        "axes.facecolor": "#222222",
        "figure.facecolor": "#222222",
        "text.color": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        }
    )
    df = delta.copy()
    df["date"] = pd.to_datetime(df["date"], utc=True)
    df["date_jst"] = df["date"].dt.tz_convert("Asia/Tokyo")
    fig, ax = plt.subplots(figsize=(10, 5))
    # plt.figure(figsize=(10, 5))
    sns.set_palette("colorblind")
    sns.lineplot(x="date_jst", y="pressure_msl", data=df, linewidth=2, ax=ax, color="#E0E0E0")
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

def show_graph(ax, label):
    legend_elements = [
    Patch(facecolor="#4FC3F7", alpha=0.3, label="Low risk"),
    Patch(facecolor="#FFB74D", alpha=0.3, label="Medium risk"),
    Patch(facecolor="#EF5350", alpha=0.3, label="High risk")
    ]  
    marker_legend = [
    Line2D([0], [0], marker=".", color="white", label="Low risk",
           markerfacecolor="none", markersize=8),
    Line2D([0], [0], marker="^", color="white", label="Medium risk",
           markerfacecolor="none", markersize=8),
    Line2D([0], [0], marker="x", color="white", label="High risk",
           markersize=8),
    ]
    ax.set_title("Atmospheric Pressure & Sudden Change Risk")
    ax.set_xlabel("Time (JST)")
    ax.set_ylabel("Pressure (hPa)")
    legend1 = ax.legend(handles=legend_elements, loc="upper right")
    ax.add_artist(legend1)
    ax.legend(handles=marker_legend, loc="upper left")

def plot_risk_markers(ax, df, risk_col):
    for risk, marker in RISK_MARKER.items():
        sub = df[df[risk_col] == risk]
        if sub.empty:
            continue
        ax.scatter(
            sub["date_jst"],
            sub["pressure_msl"],
            marker=marker,
            s=60,
            linewidths=1.5,
            facecolors="none" if marker != "x" else None,
            edgecolors="white",
            # zorder=5,
            zorder=RISK_ZORDER[risk],
            label=f"{risk} risk",
        )

# pressure_data = pd.read_csv("../storage/output.csv", parse_dates=["date"])
# sns.set_theme(style="whitegrid")
# plt.figure(figsize=(10, 5))
# sns.lineplot(x="date", y="pressure", data=pressure_data)
# plt.title("Pressure Over Time")
# plt.show()