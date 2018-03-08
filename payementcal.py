# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:55:41 2018

@author: Han Minxing
"""

import datetime
import calendar
import numpy as np
import xlrd
import pandas as pd

pd.set_option('colheader_justify', 'right')
pd.set_option('display.unicode.east_asian_width', True)

def gen_date_list(start_date, end_date):
    date_list = []
    if end_date.month >= start_date.month:
        y = 0
    else:
        y = 1
        
    months = (end_date.year - y - start_date.year)*12 + end_date.month - start_date.month + y*12
    #print(months)
    
    for i in range(months+1):
        month = start_date.month - 1 + i
        year = start_date.year + month // 12
        month = month % 12 + 1
        day = min(start_date.day,calendar.monthrange(year,month)[1])
        date_list.append(datetime.date(year,month,day))
    return date_list

#处理excel
xlrd.Book.encoding = "gbk"
file = eval(input("输入文件>>"))
book = xlrd.open_workbook(filename=file)
table = book.sheet_by_name('Sheet1')

nRows = table.nrows  
nCols = table.ncols

#if table.cell(1,3).value == 0:
#start_date = xlrd.xldate.xldate_as_datetime(table.cell(1,4).value,0)
    #start_date = xlrd.xldate.xldate_as_datetime(table.cell(1,3).value,0)
a = input('起租日>>')
start_date = datetime.datetime.strptime(a, "%Y-%m-%d")
end_date = xlrd.xldate.xldate_as_datetime(table.cell(nRows-1,4).value,0)

col = ["项目金额","保证金", "管理费", "日期", "租金"]
date_list = gen_date_list(start_date, end_date)#数列
n = len(date_list)
blank_data = np.zeros((n,5))
df = pd.DataFrame(blank_data, columns=col)
#项目金额
df.项目金额[0] = float(table.cell(1,0).value)
#保证金
df.保证金[0] = float(table.cell(1,1).value)
#管理费
df.管理费[0] = float(table.cell(1,2).value)

#第一期现金流
df.租金[0] = -df.项目金额[0] + df.保证金[0] + df.管理费[0]

df.日期 = date_list
for i in range(nRows):
    if i>0:
        date = xlrd.xldate.xldate_as_datetime(float(table.cell(i,4).value),0).strftime('%Y-%m-%d')
        #print(date)
        for j in range(len(df.index)):
            if str(df.日期[j]) == date:
                df.租金[j] = float(table.cell(i,5).value)
                if j == len(df.index)-1:
                    df.租金[j] = float(table.cell(i,5).value) - float(df.保证金[0])

#最后一期租金

print(df.租金[len(df.index)-1])

payment = df.租金.values.tolist()   
print(df)         
irr = round(np.irr(payment)*12,4)*100
print("IRR = %.2f" % irr)


        




