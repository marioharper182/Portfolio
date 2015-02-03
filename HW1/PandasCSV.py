__author__ = 'Mario'

import pandas as pd
from pandas.stats.ols import OLS as ols
import numpy as np
import os
import math

class Homework1():
    def __init__(self):
        pd.set_option('display.mpl_style', 'default')
        # figsize(15,5)

        somecsv = os.path.abspath('quiz1.csv')
        somecsv = pd.read_csv(somecsv)
        print(somecsv[:3])

        Ask = somecsv['ASK']
        Bid = somecsv['BID']
        Price = somecsv['PRC']
        Volume = somecsv['VOL']

        # somecsv.replace('VOL', '', regex=True).astype('float')/100
        somecsv['VOL'] = somecsv['VOL'].astype('float')
        spread = (Ask-Bid)/((Ask+Bid)/2)
        Spread = somecsv['Spread'] = pd.Series(spread, index=somecsv.index)
        Volume1 = np.array(Volume)
        # Volume = Volume.astype(float)
        Vollist = []
        for i in Volume1:
            try:
                A = math.log(i)
                Vollist.append(A)
            except:
                Vollist.append(0)
        # logVolume = [math.log(i) for i in Volume]
        # logVolume = math.log(Volume)
        somecsv['logVOL'] = pd.Series(Vollist, index=somecsv.index)
        Pricelist = []
        for i in Price:
            try:
                B = math.sqrt(i)
                Pricelist.append(B)
            except:
                Pricelist.append(0)

        # sqrtPrice = math.sqrt(Price)
        somecsv['sqrPRC'] = pd.Series(Pricelist, index=somecsv.index)
        X = somecsv[['logVOL', 'sqrPRC']]

        P1 = self.Problem1(spread)
        P2 = self.Problem2(Spread, Price, Volume)
        p3 = self.Problem3(Spread, X)

        print(P1)
        print(P2)

    def Problem1(self, spread):
        sp = spread
        spreadmean = np.mean(sp)
        spreadmedian = np.median(sp)
        spreadmin = np.min(sp)
        spreadmax = np.max(sp)
        spreadstd = np.std(sp)

        # This is problem 1:
        # print('spreadmean, spreadmedian, spreadmin, spreadmax, spreadstd')
        # print(spreadmean, spreadmedian, spreadmin, spreadmax, spreadstd)
        return(('Mean',spreadmean),('Median',spreadmedian),
               ('Min',spreadmin),('Max',spreadmax),
               ('StandardDev',spreadstd))

    def Problem2(self, Spread, Price, Volume):
        # Note that we do not know if we can assume normality
        sp, pr, vol = Spread, Price, Volume
        # stats.pearsonr(sp, pr)
        # stats.pearsonr(sp, vol)
        part1 = sp.corr(pr)
        part2 = sp.corr(vol)
        return part1, part2

    def Problem3(self, Spread, X):
        sp, x = Spread, X

        # reg = ols(y=sp, x=(math.log(vol),math.sqrt(pr)))
        reg = ols(y=sp, x=x)
        print(reg)

def main():
    Homework1()
if __name__ == '__main__':
    main()