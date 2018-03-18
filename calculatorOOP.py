# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:31:03 2018

@author: Han
"""
import numpy as np
import pandas as pd


class Quotation():    
    def __init__(self, capital, financial_margin_rate, service_charge_rate, req_irr):
        self.capital = capital
        self.financial_margin_rate = financial_margin_rate
        self.service_charge_rate = service_charge_rate
        self.financial_margin = self.capital * self.financial_margin_rate
        self.service_charge = self.capital * self.service_charge_rate
        self.req_irr = req_irr
        self._setPayRule()
        self._setIRRRange()
        self._setWithDrawCap()
        
    #设置还款方式，默认5年季度付 等额
    def _setPayRule(self, year=5, freq=4, every_pay=0):        
        self.year = year
        self.freq = freq
        self.every_pay = every_pay
        self.paytimes = self.year * self.freq
    #设置可接受的IRR范围    
    def _setIRRRange(self, min_irr=None, max_irr=None):
            self.min_irr = min_irr
            self.max_irr = max_irr
    #设置可接受的年利率范围
    def _setAnualRate(self,min_anual_rate,max_anual_rate):
        pass
    #设置回收本金范围
    def _setWithDrawCap(self, p_withdraw=0.3, withdraw_year=2):
        self.p_withdraw = p_withdraw
        self.min_p_withdraw = self.p_withdraw * 1/15
        self.max_p_withdraw = self.p_withdraw * 17/15
        self.withdraw_year = withdraw_year
    
    def generate(self):
        if self.freq == 4 and self.every_pay == 0:
            #pay = first_cashflow/sum((1+irr)**n)
            _times = np.arange(self.paytimes)+1
            
            pay = ((-(-self.capital+self.financial_margin+self.service_charge)) + (self.service_charge*((1+self.req_irr/self.paytimes)**_times[-1])))/(((1/((1+self.req_irr/4))**_times).sum()))
            print(pay)

            
        
a = Quotation(1000000,0.05,0.03,0.1)
print(a.year,a.freq,a.paytimes)

a.generate()

