# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext,Menu
from tkinter import messagebox as mBox

win = tk.Tk()

win.title("IRR calculator")
win.resizable(0,0)
mainFrame = ttk.LabelFrame(win, text="@author: Hanminxing")
mainFrame.grid(column=0, row=0,columnspan=4,rowspan=7, padx=8, pady=6)

 
projectReqments = ["Total Money","Guarentee Fee","Service Fee","StartDate"]
itemMoney = ['a','b','c','d']

for req in range(len(projectReqments)):
    ttk.Label(mainFrame, text=projectReqments[req]+" :").grid(column=0, row=[req])
    itemMoney[req] = tk.StringVar()
    ttk.Entry(mainFrame, width=20, textvariable=itemMoney[req]).grid(column=1, row=req, padx=4,pady=3, sticky=tk.W)

ttk.Label(mainFrame, text="Date n money :").grid(column=2,row=0,padx=4,pady=3,sticky=tk.W)
scr = scrolledtext.ScrolledText(mainFrame,width=30, height=5, wrap=tk.WORD)
scr.grid(column=2,row=1,columnspan=2,rowspan=3, padx=4,pady=3)

results = ttk.Label(mainFrame, text="IRR = ")
results.grid(column=2,padx=4,pady=3,sticky=tk.E)

irr_res = tk.Entry(mainFrame,text="")
irr_res.grid(column=3,row=4,padx=4,pady=3,sticky=tk.W)


Reqment = {}
dates_rents_l = []

def submit():
    global dates_rents_l, Reqment
    Reqment = {}
    dates_rents_l = []
    
    for req in range(4):
        Reqment[projectReqments[req]] = itemMoney[req].get()
        
    dates_rents = scr.get(1.0, tk.END).split("\n")
    for date_rent in dates_rents:
        if len(date_rent) != 0:
            dates_rents_l.append(date_rent.split("\t"))
    
    results.configure(text=dates_rents_l)
    irr_res.insert(1,"123123")
    irr_res.configure(state='readonly')
    print(Reqment, dates_rents_l)


submit = ttk.Button(mainFrame, text="submit", command=submit).grid(column=0,row=4,padx=4,pady=3)









def _msgBox():
    mBox.showinfo('帮助', '例:\n项目金额：100000000\n保证金:2000000\n管理费：1000000\n起租日：2018-08-08\n日期和租金：（直接从报价表中粘贴还款日和租金项即可）\n点击“提交”')   

menuBar = Menu(win)
win.config(menu=menuBar)
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)


win.mainloop()   

