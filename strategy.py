from indicators import *

class Strategy:
    def __init__(self, data):
        self.data = data


class Smacrossover(Strategy):
    def run(self):
        data = self.data['close']
        sma1 = sma(data, 9)
        sma2 = sma(data, 21)

        if crossover(sma1, sma2):
            return 1
        
        elif crossover(sma2, sma1):
            return -1
        else:
            return 0