from trader import Trader
from strategy import *
import json
import bitmex


if __name__ == '__main__':
    cfg = json.load(open('cfg.txt', 'r'))
    print(f'Iniciando estratégia {cfg["strategy"]}')
    client = bitmex.bitmex(test=cfg["test"], api_key=cfg["api_key"], api_secret=cfg["api_secret"])
    exec(f'strategy = {cfg["strategy"]}')
    trader = Trader(strategy=strategy, client=client, lot=cfg["lot"], loop=cfg["loop"])
    trader.run_loop()
    