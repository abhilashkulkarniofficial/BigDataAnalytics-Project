#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:27:23 1518

@author: abhilashsk
"""

from Analytics_backend import *
from Tkinter import *
from Display_graph import *
from Query_backend import *

class Analysis_Window(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.display_widgets()
        self.data=self.get_data()
        self.configure(bg="lightblue")
        self.connection=connect_to_client()

    def display_widgets(self):
        Label(self,text="Plotting data",bg="lightblue",font="times 16 bold italic").grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=2,sticky=W)
        
        self.type_graph=StringVar()
        Label(self,bg="lightblue",text="Scatter Plot",width=15).grid(row=49,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="GrLivArea vs SalePrice",variable=self.type_graph,value='1').grid(row=49,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="TotalBsmtSF vs SalePrice",variable=self.type_graph,value='2').grid(row=49,column=2,sticky=W)

        Label(self,bg="lightblue",text="Box Plot",width=15).grid(row=50,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="OverallQual vs SalePrice",variable=self.type_graph,value='3').grid(row=50,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="YearBuilt vs SalePrice",variable=self.type_graph,value='4').grid(row=50,column=2,sticky=W)
        
        Label(self,bg="lightblue",text="Correlation Plot",width=15).grid(row=51,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="Correlation matrix (heatmap style)",variable=self.type_graph,value='5').grid(row=51,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="'SalePrice' correlation matrix",variable=self.type_graph,value='6').grid(row=51,column=2,sticky=W)
        
        Label(self,bg="lightblue",text="Scatter Plot Matrix",width=15).grid(row=52,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="SalePrice and Correlated variables",variable=self.type_graph,value='7').grid(row=52,column=1,sticky=W)
        
        Label(self,bg="lightblue",text="SalePrice",width=15).grid(row=53,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="Normal",variable=self.type_graph,value='8').grid(row=53,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="Logarithmic",variable=self.type_graph,value='9').grid(row=53,column=2,sticky=W)
        
        Label(self,bg="lightblue",text="GrLivArea",width=15).grid(row=54,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="Normal",variable=self.type_graph,value='10').grid(row=54,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="Logarithmic",variable=self.type_graph,value='11').grid(row=54,column=2,sticky=W)
        
        Label(self,bg="lightblue",text="TotalBsmtSF",width=15).grid(row=55,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="Normal",variable=self.type_graph,value='12').grid(row=55,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="Logarithmic",variable=self.type_graph,value='13').grid(row=55,column=2,sticky=W)
        
        Label(self,bg="lightblue",text=" ").grid(row=48,column=0,sticky=W)
        self.btn1=Button(self,font="Georgia 10 bold ",text="PLOT",command=self.displayGraph)
        self.btn1.grid(row=48,column=1,columnspan=2,sticky=N)
        
        Label(self,text="CRUD Operations",bg="lightblue",font="times 16 bold italic").grid(row=56,column=0,columnspan=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=2,sticky=W)
                
        Label(self,text="SalePrice",bg="lightblue",width=15).grid(row=58,column=0,sticky=W)
        self.entry1=Entry(self)
        self.entry1.grid(row=58,column=1,sticky=W)
        
        Label(self,text="TotalBsmtSF",bg="lightblue",width=15).grid(row=58,column=2,sticky=W)
        self.entry2=Entry(self)
        self.entry2.grid(row=58,column=3,sticky=W)
        
        Label(self,text="OverallQual",bg="lightblue",width=15).grid(row=60,column=0,sticky=W)
        self.entry3=Entry(self)
        self.entry3.grid(row=60,column=1,sticky=W)
        
        Label(self,text="GrLivArea",bg="lightblue",width=15).grid(row=60,column=2,sticky=W)
        self.entry4=Entry(self)
        self.entry4.grid(row=60,column=3,sticky=W)
        
        Label(self,text="RowNum",bg="lightblue",width=15).grid(row=61,column=1,sticky=W)
        self.entry5=Entry(self)
        self.entry5.grid(row=61,column=2,sticky=W)
        
        self.btn1=Button(self,font="Georgia 10 bold ",text="Insert",command=self.insertVals)
        self.btn1.grid(row=70,column=0,sticky=N)
        
        self.btn1=Button(self,font="Georgia 10 bold ",text="Update",command=self.updateVals)
        self.btn1.grid(row=70,column=1,sticky=N)
        
        self.btn1=Button(self,font="Georgia 10 bold ",text="Delete",command=self.deleteVals)
        self.btn1.grid(row=70,column=2,sticky=N)
        
        self.btn1=Button(self,font="Georgia 10 bold ",text="Fetch Data",command=self.fetchVals)
        self.btn1.grid(row=70,column=3,sticky=N)
        
        Label(self,text="Analytics Results",bg="lightblue",font="times 16 bold italic").grid(row=71,column=0,columnspan=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",bg="lightblue",width=15).grid(row=0,column=2,sticky=W)
        
        self.row_name=StringVar()
        Label(self,bg="lightblue",text="Data Field",width=15).grid(row=72,column=0,sticky=W)
        Radiobutton(self,bg="lightblue",text="SalePrice",variable=self.row_name,value='SalePrice').grid(row=72,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="TotalBsmtSF",variable=self.row_name,value='TotalBsmtSF').grid(row=72,column=2,sticky=W)
        Radiobutton(self,bg="lightblue",text="GrLivArea",variable=self.row_name,value='GrLivArea').grid(row=72,column=3,sticky=W)
        
        self.btn1=Button(self,font="Georgia 10 bold ",text="Fetch Stats",command=self.getStats)
        self.btn1.grid(row=73,column=3,sticky=N)
        
        

    def displayGraph(self):
        if self.type_graph.get():
            displayGraph(self.type_graph,self.data)
            text=getDescription(self.type_graph)
            print(text)
    
    def insertVals(self):
        entry1=self.entry1.get()
        entry2=self.entry2.get()
        entry3=self.entry3.get()
        entry4=self.entry4.get()
        
        data=fetch_data(self.connection,4)
        data=data[0]
        data['SalePrice']=int(entry1)
        data['TotalBsmtSF']=int(entry2)
        data['OverallQual']=int(entry3)%10
        data['GrLivArea']=int(entry4)
        data['_id']=self.connection.count()+1
        
        print(data['_id'])
        
        create_entry(self.connection,data)
        
    def updateVals(self):
        entry1=self.entry1.get()
        entry2=self.entry2.get()
        entry3=self.entry3.get()
        entry4=self.entry4.get()
        entry5=self.entry5.get()
        
        data=fetch_data(self.connection,int(entry5))
        data=data[0]
        data['SalePrice']=int(entry1)
        data['TotalBsmtSF']=int(entry2)
        data['OverallQual']=int(entry3)%10
        data['GrLivArea']=int(entry4)
        
        print(data['_id'])
        
        update_entry(self.connection,data,int(entry5))
        
    def deleteVals(self):
        entry5=int(self.entry5.get())
        
        delete_entry(self.connection,entry5)
        
    def fetchVals(self):
        entry5=int(self.entry5.get())
        data=fetch_data(self.connection,entry5)
        data=data[0]
        
        y=[self.entry1,self.entry2,self.entry3,self.entry4]
        desc=[data['SalePrice'],data['TotalBsmtSF'],data['OverallQual'],data['GrLivArea']]
        for i,x in enumerate(y):
            x.config(state=NORMAL)
            x.delete(0,END)
            x.insert(0,desc[i])
            x.config(state=DISABLED)
        
    def getStats(self):
        col=self.row_name.get()
        print(self.data[col].describe())
        

    def get_data(self):
        try:
            data=read_data()
            data=clean_data(data)
        except:
            data=read_from_mongo()
        return data

    
        
        
        


root=Tk()
root.title("Data analysis of House Price Dataset")
root.geometry("850x500")
root.configure(bg="lightblue")
app=Analysis_Window(root)
root.mainloop()