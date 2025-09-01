import pandas as pd
import requests

def load_historical_data(path="Data/Data_Clean.xlsx"):
    """Load historical dataset."""
    return pd.read_excel(path)

def get_live_price(symbol="BTCUSDT"):
    """Fetch live crypto price from Binance."""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url).json()
        return float(response['price'])
    except:
        return "Error fetching live price"
