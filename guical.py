# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, Menu

win = tk.Tk()

win.title("IRR calculator")

mainFrame = ttk.LabelFrame(win, text="IRR calculator")
mainFrame.grid(column=0, row=0, padx=8, pady=6)

projectReqments = ["Total Money","Guarentee Fee","Service Fee","StartDate"]
itemMoney = ['a','b','c','d']

for req in range(len(projectReqments)):
    ttk.Label(mainFrame, text=projectReqments[req]+" :").grid(column=0, row=[req])
    itemMoney[req] = tk.StringVar()
    ttk.Entry(mainFrame, width=20, textvariable=itemMoney[req]).grid(column=1, row=req, padx=4,pady=3, sticky=tk.W)

ttk.Label(mainFrame, text="Date n money :").grid(column=0, row=len(projectReqments)*2,padx=4,pady=3)
scr = scrolledtext.ScrolledText(mainFrame,width=30, height=10, wrap=tk.WORD)
scr.grid(column=0,columnspan=2, padx=4,pady=3)

Reqment = {}
dates_rents_l = []
def submit():
    global dates_rents_l
    for req in range(4):
        Reqment[projectReqments[req]] = itemMoney[req].get()
    dates_rents = scr.get(1.0, tk.END).split("\n")
    for date_rent in dates_rents:
        if date_rent != None:
            dates_rents_l.append(date_rent.split("\t"))
    print(Reqment, dates_rents_l)




  
submit = ttk.Button(mainFrame, text="submit", command=submit).grid(column=0, sticky='SWE')


win.mainloop()   

