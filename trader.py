import requests
import pandas as pd
from strategy import *
import time
from datetime import datetime



class Trader:   
    def __init__(self, symbol, client, strategy, lot, loop):
        self.symbol = symbol
        self.client = client
        self.strategy = strategy
        self.lot = lot
        self.loop = loop


    def run_loop(self):
        while True:
            try:
                url = f"https://www.bitmex.com/api/v1/trade/bucketed?binSize=1d&partial=false&symbol={self.symbol}&count=100&reverse=false"
                rsp = pd.read_json(url)
                strategy = self.strategy(rsp[::-1])
                signal = strategy.run()
                if signal == 1:
                    order = self.client.Order.Order_new(symbol=self.symbol, orderQty=self.lot, ordType="Market").result()
                    print(order, 'order buy')
                elif signal == -1:
                    order = self.client.Order.Order_new(symbol=self.symbol, orderQty=-self.lot, ordType="Market").result()
                    print(order, 'order sell')
                print(datetime.utcnow().replace(microsecond=0), f'signal: {signal} esperando o proximo signal')
                time.sleep(self.loop)
            except Exception as e:
                print(e)
