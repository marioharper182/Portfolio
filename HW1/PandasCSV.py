__author__ = 'Mario'

import pandas as pd
from pandas.stats.ols import OLS as ols
import numpy as np
import os
import math
import textwrap

class Homework1():
    def __init__(self):
        pd.set_option('display.mpl_style', 'default')

        somecsv = os.path.abspath('quiz1.csv')
        somecsv = pd.read_csv(somecsv)

        Ask = somecsv['ASK']
        Bid = somecsv['BID']
        Price = somecsv['PRC']
        Volume = somecsv['VOL']

        somecsv['VOL'] = somecsv['VOL'].astype('float')
        spread = (Ask-Bid)/((Ask+Bid)/2)
        Spread = somecsv['Spread'] = pd.Series(spread, index=somecsv.index)
        Volume1 = np.array(Volume)

        # Build the parameters for part 3
        Vollist = []
        Pricelist = []
        for i in Volume1:
            try:
                A = math.log(i)
                Vollist.append(A)
            except:
                Vollist.append(0)
        for i in Price:
            try:
                B = math.sqrt(i)
                Pricelist.append(B)
            except:
                Pricelist.append(0)
        somecsv['logVOL'] = pd.Series(Vollist, index=somecsv.index)
        somecsv['sqrPRC'] = pd.Series(Pricelist, index=somecsv.index)
        X = somecsv[['logVOL', 'sqrPRC']]

        P1 = self.Problem1(spread)
        P2 = self.Problem2(Spread, Price, Volume)
        P3 = self.Problem3(Spread, X)
        print('<Summary Statistics>', P1)
        print('<Pearson Correlation Coefficient>', P2)
        print(P3)
        self.Problem4()

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
        return(reg)

    def Problem4(self):
        print(textwrap.dedent("""
            We see that there is a negative correlation between
            volume,price (adjusted) and the expected spread.
            We propose that by increasing the trading volume or
            the price of the trading material, we should see
            greater liquidity in the market from a decrease in
            spread."""))

def main():
    Homework1()
if __name__ == '__main__':
    main()