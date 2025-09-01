def generate_signal(ma_short, ma_long):
    """Generate trading signal based on moving averages."""
    if ma_short > ma_long:
        return "BUY"
    elif ma_short < ma_long:
        return "SELL"
    else:
        return "HOLD"
