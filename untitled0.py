# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:07:22 2018

@author: Han
"""

import matplotlib.pyplot as plt
import numpy as np


irr = 0.1000
x = 1000000
b = 30000

year = np.arange(5) + 1
pay = (x-b+b*(1+irr)**year[-1])/((1/(1+irr)**year).sum())


a = [pay]*year[-1]
a[-1] = pay-b
#新现金流
x = [-x+b]+ a
print(pay,x,np.irr(x))

