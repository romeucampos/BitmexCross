import requests
import pandas as pd
import pandas_datareader as web


def crossover(serie1, serie2):
    return True if serie1[-2] > serie2 and serie1[-1] < serie2 else False

class Strategy:
    def __init__(self, data):
        self.data = data





class BB(Strategy):
    def bollinger(self, window=20, d=2):
        close = self.data['Close']
        mean = close.rolling(window).mean()
        std = close.rolling(window).std()
        upper = mean + (std * d)
        lower = mean - (std * d)
        return upper, lower



class Trader:
    def __init__(self, client, strategy):
        self.client = client
        self.strategy = strategy

    def run_trader(self):
        ...

if __name__ == '__main__':
    BTCUSD = web.get_data_yahoo('BTC-USD', start='2019-1-1')
    bb = BB(BTCUSD)
    bb.bollinger()
