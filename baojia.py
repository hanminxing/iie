# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:40:08 2018

@author: Han Minxing
"""
import numpy as np

payment = []

TotalMoney = 100000000
Baozhengjin = TotalMoney * 0.03
Guanlifei = TotalMoney * 0.05
Cishu = 10

while True:
    a = np.random.randint(TotalMoney*0.08,TotalMoney*0.17,Cishu)
   
    xjl = -TotalMoney + Baozhengjin +Guanlifei
    d = a.tolist()
    d.insert(0,xjl)
    d[10] = d[10] - Baozhengjin
    lilv = (sum(d)+Guanlifei)/TotalMoney/5
    container = list(np.zeros(5*10))
    for n in range(11):
        container.insert(6*n, d[n])        
    b = (a[0]+a[1]+a[2]+a[3])/(1 + lilv)
    c = b/TotalMoney * 100 # C>30
    
    
    irr = np.irr(container)*12*100
    
    print(irr,d)
    if 9.49 < irr < 9.52:
        if 28< c <35:
            print(d,c,irr,(sum(d)+Guanlifei)/TotalMoney/5)
            break
   
    
