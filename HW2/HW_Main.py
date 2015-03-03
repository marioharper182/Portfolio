__author__ = 'HarperMain'
import pandas as pd
from pandas.stats.ols import OLS as ols
import numpy as np
import os
from pylab import *

class HW2():
    def __init__(self):
        # self.Problem1()
        # self.Problem3()
        # self.Problem4()
        self.Problem5()

    def Problem1(self):
        t = arange(0.0, 2.0, 0.01)
        s = t - 1
        d = -t + 1
        s2 = t -2

        supply1 = plt.plot(t, s, label = 'Initial Supply')
        demand = plt.plot(t, d, label = 'Demand')
        supply2 = plt.plot(t, s2, label = 'New Supply')

        xlabel('Lendable Funds')
        ylabel('Interest Rates')
        title('Fed decisions on Macroeconomics')
        plt.legend(loc=4)
        grid(True)
        savefig("FedDecision.png")
        # show()

    def Problem3(self):
        somecsv = os.path.abspath('Macrodata_Quiz.csv')
        somecsv = pd.read_csv(somecsv)
        GDPChg = somecsv['GDPChg']
        reg = ols(y=GDPChg, x=somecsv[['ConsChg','UnempChg']])
        print reg

    def Problem4(self):
        print "Problem 4:"
        somecsv = os.path.abspath('IBM+Debt-to-Equity.csv')
        somecsv = pd.read_csv(somecsv)
        Mkvalt = somecsv['mkvaltq']
        atq, ltq = somecsv['atq'],somecsv['ltq']
        D_E = atq-ltq
        D_E2 = D_E**2
        DE = somecsv['D_E'] = pd.Series(D_E, index=somecsv.index)
        DE = somecsv['D_E2'] = pd.Series(D_E2, index=somecsv.index)
        reg = ols(y=Mkvalt, x=somecsv[['D_E','D_E2']])
        print 'Part A'
        print reg

        print 'Part B'
        ansB = 25.4802/.0006
        print "The ideal ratio appears to be ", ansB

    def Problem5(self):
        print "Problem 5:"
        somecsv = os.path.abspath('finstatement_quiz2.csv')
        somecsv = pd.read_csv(somecsv)
        roe = somecsv['roe']
        D_E = somecsv['totassets']-somecsv['totliab']
        DE = somecsv['DE'] = pd.Series(D_E, index=somecsv.index)
        tat = somecsv['tat']
        pm = somecsv['pm']

        reg = ols(y=roe, x=somecsv[['DE', 'tat', 'pm']])
        print "Part A:",reg
        # print somecsv.columns.values
        print "Part B: It would seem that ROE is positively " \
              "correlated most with tat and then with DE. But the " \
              "negatively correlated pm is more significant than DE " \
              "albeit negative."

        # print somecsv.sort(['roe'], ascending=[0])
        # print somecsv.sort(['pm'], ascending=[0])
        print somecsv.sort(['tat'], ascending=[0])
        print 'Problem 6: \n' 'Roe: FWM, MPAA, MSB \n''pm: MNELF, SNET, BSHF \n''tat: 3COSR, AMRK, SPGZ'



def main():
    HW2()
if __name__ == '__main__':
    main()
