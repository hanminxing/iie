# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import ttk,scrolledtext,Menu
from tkinter import messagebox as mBox

import datetime
from calendar import monthrange
import numpy as np
import pandas as pd


#calculator core
pd.set_option('colheader_justify', 'right')
pd.set_option('display.unicode.east_asian_width', True)

#date list generator
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
        day = min(start_date.day,monthrange(year,month)[1])
        date_list.append(datetime.date(year,month,day))
    return date_list

#date_pattern = re.compile()

#calculator GUI
win = tk.Tk()

win.title("IRR calculator v1.0 beta")
win.resizable(0,0)
mainFrame = ttk.LabelFrame(win, text="@author: Hanminxing")
mainFrame.grid(column=0, row=0,columnspan=4,rowspan=7, padx=8, pady=6)
 
projectReqments = ["Capital","Financial Margin","Service Charge","Commencement Date"]
itemMoney = ['a','b','c','d']

for req in range(len(projectReqments)):
    ttk.Label(mainFrame, text=projectReqments[req]+" :").grid(column=0, row=[req])
    itemMoney[req] = tk.StringVar()
    ttk.Entry(mainFrame, width=20, textvariable=itemMoney[req]).grid(column=1, row=req, padx=4,pady=3, sticky=tk.W)

ttk.Label(mainFrame, text="Pay Day and Payment :").grid(column=2,row=0,padx=4,pady=3,sticky=tk.W)
scr = scrolledtext.ScrolledText(mainFrame,width=30, height=5, wrap=tk.WORD)
scr.grid(column=2,row=1,columnspan=2,rowspan=3, padx=4,pady=3)

results = ttk.Label(mainFrame, text="IRR = ")
results.grid(column=2,padx=4,pady=3,sticky=tk.E)

irr_res = tk.Entry(mainFrame,text="")
irr_res.grid(column=3,row=4,padx=4,pady=3,sticky=tk.W)


Reqment = {}
dates_rents_l = []

#submit button
def submit():

    global dates_rents_l, Reqment
    Reqment = {}
    dates_rents_l = []
    
    irr_res.delete(0, tk.END)
    for req in range(4):
        Reqment[projectReqments[req]] = itemMoney[req].get()
        
    dates_rents = scr.get(1.0, tk.END).split("\n")
    for date_rent in dates_rents:
        if len(date_rent) != 0:
            dates_rents_l.append(date_rent.split("\t"))
    
    start_date = datetime.datetime.strptime(Reqment['StartDate'], "%Y/%m/%d")
    end_date = datetime.datetime.strptime(dates_rents_l[-1][0],"%Y/%m/%d")
    
    col = ["项目金额","保证金", "管理费", "日期", "租金"]
    date_list = gen_date_list(start_date, end_date)#数列
    n = len(date_list)
    blank_data = np.zeros((n,5))
    df = pd.DataFrame(blank_data, columns=col)

    df.项目金额[0] = float(Reqment['Total Money'].replace(",",""))
    df.保证金[0] = float(Reqment['Guarentee Fee'].replace(",",""))
    df.管理费[0] = float(Reqment['Service Fee'].replace(",",""))
    #第一期现金流
    df.租金[0] = -df.项目金额[0] + df.保证金[0] + df.管理费[0]
    
    df.日期 = date_list
    
    #填写对应日期的租金
    for i in range(len(dates_rents_l)):
            dates = datetime.datetime.strptime(dates_rents_l[i][0],'%Y/%m/%d')
            #print(date.date(), dates_rents_l[i][1])
            for j in range(len(df.index)):
                #print(df.日期[j], date.date())
                if df.日期[j] == dates.date():
                    df.租金[j] = float(dates_rents_l[i][1].replace(",",""))
                    #print(dates_rents_l[i][1])
                    if j == len(df.index)-1:
                        df.租金[j] = float(dates_rents_l[i][1].replace(",","")) - float(df.保证金[0])
                        
    payment = df.租金.values.tolist()   
    #print(payment)         
    irr = round(np.irr(payment)*12,4)*100
    #print("IRR = %.2f" % irr)
    
    irr_res.insert(0,irr)
    #irr_res.configure(state='readonly')
    #print(start_date, end_date,dates_rents_l)











submit = ttk.Button(mainFrame, text="submit", command=submit).grid(column=0,row=4,padx=4,pady=3)








def _msgBox():
    mBox.showinfo('帮助', '例:\n项目金额：100000000\n保证金:2000000\n管理费：1000000\n起租日：2018/08/08\n日期和租金：（直接从报价表中粘贴还款日和租金项即可）\n点击“提交”')   

menuBar = Menu(win)
win.config(menu=menuBar)
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)


win.mainloop()   

