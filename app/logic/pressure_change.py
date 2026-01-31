def add_pressure_delta_inplace(df, windows, col="pressure_msl"):
    """Add dp_* columns to df (in-place)."""
    for label, hours in windows.items():
        df[f"dp_{label}"] = df[col].diff(hours)
    
def calc_risk_from_delta_pressure(dp, RISK_CONFIG):
    if dp <= RISK_CONFIG["down"]["high"]:
        return "high"
    elif dp <= RISK_CONFIG["down"]["medium"]:
        return "medium"
    elif dp <= RISK_CONFIG["down"]["low"]:
        return "low"
    elif dp >= RISK_CONFIG["up"]["high"]:
        return "high"
    elif dp >= RISK_CONFIG["up"]["medium"]:
        return "medium"
    elif dp >= RISK_CONFIG["up"]["low"]:
        return "low"
    else:
        return "none"
