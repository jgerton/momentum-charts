import plotly.graph_objects as go

def plot_candlestick(df, symbol):
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name=symbol
    )])

    fig.update_layout(
        title=f'{symbol} Candlestick Chart',
        yaxis_title='Price',
        xaxis_title='Date',
        xaxis_rangeslider_visible=False
    )

    fig.show()
