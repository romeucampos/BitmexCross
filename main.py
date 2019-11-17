from trader import Trader
from strategy import *
import json
import bitmex


if __name__ == '__main__':
    print(f'Carregando estratégia {cfg["strategy"]}')
    client = bitmex.bitmex(test=cfg["test"], api_key=cfg["api_key"], api_secret=cfg["api_secret"])
    exec(f'strategy = {cfg["strategy"]}')
    trader = Trader(symbol=cfg["symbol"], strategy=strategy, client=client, lot=cfg["lot"], loop=cfg["loop"])
    trader.run_loop()