import pandas as pd

def add_pressure_delta_inplace(df, windows, col="pressure_msl"):
    """Add dp_* columns to df (in-place)."""
    for label, hours in windows.items():
        df[f"dp_diff_{label}"] = df[col].diff(hours)
        rolling = df[col].rolling(hours)
        df[f"dp_range_{label}"] = rolling.max() - rolling.min()
    


def calc_risk_from_delta_pressure(dp_diff, dp_range, config):
    if pd.isna(dp_diff) or pd.isna(dp_range):
        return "none"

    if abs(dp_diff) >= config["diff"]["high"] or dp_range >= config["range"]["high"]:
        return "high"
    if abs(dp_diff) >= config["diff"]["med"] or dp_range >= config["range"]["med"]:
        return "med"
    if abs(dp_diff) >= config["diff"]["low"] or dp_range >= config["range"]["low"]:
        return "low"

    return "none"
