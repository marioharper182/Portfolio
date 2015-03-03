__author__ = 'HarperMain'
from math import *
import matplotlib.pyplot as plt
from pylab import *

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
show()