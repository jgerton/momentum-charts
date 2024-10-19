from data.api_client import SchwabAPIClient
from indicators.technical_indicators import add_indicators
from charts.charting import plot_candlestick
import pandas as pd

def main():
    # Initialize API client
    client = SchwabAPIClient()

    # Define parameters
    symbol = 'AAPL'  # Example symbol
    start_date = '2023-01-01'
    end_date = '2023-10-19'

    # Fetch data
    stock_data = client.get_stock_data(symbol, start_date, end_date)

    # Convert data to DataFrame
    df = pd.DataFrame(stock_data['prices'])
    df['date'] = pd.to_datetime(df['date'])

    # Calculate technical indicators
    df = add_indicators(df)

    # Plot candlestick chart
    plot_candlestick(df, symbol)

if __name__ == '__main__':
    main()
