# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:12:15 2018

@author: Han Minxing
"""

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt


#total, years, times, irr, modes=1,2,4
class Quotation():
    def __init__(self, total, year,mode,irr):
        self.total = total
        self.year = year
        self.irr = irr
        self.mode = mode
        self.times = year * mode
        

        
    #生成报价    
    def generate(self,bzj,glf):
        col = ["Dates","Payment"]
        freq = {4:'3M',2:'6M',1:'12M'}
        dates = pd.date_range('2000-1-1',periods=self.times,freq=freq[self.mode])
        blank_frame = pd.DataFrame(np.zeros((self.times,2)),columns=col)
        blank_frame['Dates'] = dates
        
        self.bzj = self.total *bzj
        self.glf = self.total *glf
        
        years = np.arange(self.year)+1
        x = (self.total-self.bzj-self.glf)/((1+self.irr)**years).sum()
        print(x)
        
        y_var = []
        x_var = []
        
        
        for i in range(500):
            
            ary = [round(x,2)]*self.times
            irr_ary = [-self.total+self.bzj+self.glf] + ary
            irr_ary[-1] = irr_ary[-1] -self.bzj
            etd_irr = round(np.irr(irr_ary)*self.mode,4)
            blank_frame['Payment']=ary
            x_var.append(i)
            y_var.append(etd_irr)
            print("IRR="+str(etd_irr*100)+"\n每期租金："+str(round(x,2))+" 元")
            #x的位数
            
            if etd_irr==self.irr:
                break            
            
            elif etd_irr>self.irr*1.01:
                x -= 100000 
            elif etd_irr>self.irr*1.001:
                x -= 10000
            elif etd_irr>self.irr*1.0001:
                x -= 1000
            elif etd_irr>self.irr*1.00001:
                x -= 100
            elif etd_irr>self.irr*1.000001:
                x -= 10
            elif etd_irr>self.irr*1.0000001:
                x -= 1
            elif etd_irr<self.irr*0.99:
                x += 100000 
            elif etd_irr<self.irr*0.999:
                x += 10000 
            elif etd_irr<self.irr*0.9999:
                x += 1000 
            elif etd_irr<self.irr*0.99999:
                x += 100 
            elif etd_irr<self.irr*0.999999:
                x += 10 
            elif etd_irr<self.irr*0.9999999:
                x += 1 


                
            plt.plot(x_var, y_var)
            plt.show()
            
        print("项目金额: "+str(self.total)+" 元\n"+"管理费: "+str(self.glf)+" 元\n"+"保证金: "+str(self.bzj)+" 元\n")
        print(blank_frame)



        
        
a=Quotation(50000000,5,4,0.1105000)
before = time.time()
a.generate(0.04,0.05)
after = time.time()
print('用时 '+ str(round(after-before,4))+' s')
print()

