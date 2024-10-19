import pandas as pd
import pandas_ta as ta

def add_indicators(df):
    # Add RSI
    df['RSI'] = ta.rsi(df['close'], length=14)
    # Add ATR
    df['ATR'] = ta.atr(high=df['high'], low=df['low'], close=df['close'], length=14)
    # Add other indicators as needed
    return df
