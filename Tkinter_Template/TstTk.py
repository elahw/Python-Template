#! /usr/bin/env python2.7

import os, re, sys
import Tkinter as tk
import tkMessageBox



def TstTkinter():
    master = tk.Tk()
    master.title("Randon Instructions Generate")
    #master.geometry("500x600")

    tk.Label(master, text="--rand_num =").grid(row=0,column=0, sticky="E")
    tk.Label(master, text="--jcc_num  =").grid(row=1,column=0, sticky="E")
    tk.Label(master, text="--ind_num  =").grid(row=2,column=0, sticky="E")
    tk.Label(master, text="--dir_num  =").grid(row=3,column=0, sticky="E")
    
    varb = tk.StringVar(value="1024") # default value is 1024
    e1 = tk.Entry(master, textvariable=varb)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e1.grid(row=0,column=1,padx=10, pady=5)
    e2.grid(row=1,column=1,padx=10, pady=5)
    e3.grid(row=2,column=1,padx=10, pady=5)
    e4.grid(row=3,column=1,padx=10, pady=5)

    def show():
        print e1.get()
        print e2.get()
        print e3.get()
        print e4.get()
        e1.delete(0,"end")
    def tanchuang():
        tkMessageBox.showinfo(title="Confirm Info", message="hello world")
        master.quit()
    
    tk.Button(master,text="Ok",width=10, command=tanchuang   ).grid(row=4, column=0, sticky="w",padx=10, pady=5)
    tk.Button(master,text="No",width=10, command=master.quit ).grid(row=4, column=1, sticky="W",padx=10, pady=5)


    master.mainloop()
TstTkinter()

