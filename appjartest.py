# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:55:44 2018

@author: Han Minxing
"""

from appJar import gui

app = gui("calculator","400x600")

app.startLabelFrame("项目条款")
app.addLabelEntry("项目金额",0,1,4)
app.addLabelEntry("保证金",1,1,4)
app.addLabelEntry("管理费",2,1,4)
app.addLabelEntry("起租日",3,1,4)
app.setEntryDefault("起租日", "年-月-日")
app.setFocus("项目金额")
app.stopLabelFrame()



app.startTabbedFrame("日期和租金")
app.startTab("日期和租金")
app.addTextArea("t1")
app.stopTab()
app.stopTabbedFrame()




app.go()



