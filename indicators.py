import pandas as pd


def crossover(serie1, serie2):
    serie1 = pd.Series(serie1)    
    serie2 = pd.Series(serie2)
    return serie1.values[-2] < serie2.values[-2] and serie1.values[-1] > serie2.values[-1] 


def cross(series1, series2):
    return crossover(series1, series2) or crossover(series2, series1) 


def sma(array, n):
    return pd.Series(array).rolling(n).mean()


def bollinger(array, n, desv):
    mean = sma(array, n)
    std = pd.Series(array).rolling(n).std()
    return mean * (std + desv)


def bollinger_s(array, n, desv):
    mean = sma(array, n)
    std = pd.Series(array).rolling(n).std()
    lower = mean - (std * desv)
    upper = mean + (std * desv)
    return upper, lower 
