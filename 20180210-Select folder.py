# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:08:12 2018

@author: ustci

Todolist:
    - select folder (on-going)
    - enter the label (on-going)
    - plot the graph
    - some more
"""

import tkinter as tk
import tkinter.filedialog
import data_sets_class

#import tkinter.filedialog
# import tkinter.messagebox
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def select_folder(folder_name_tk):
    '''
    folder_name_tk: tk.StringVar()
    function: set folder_name to fname
    '''
    fname = tk.filedialog.askdirectory()
    folder_name_tk.set(fname)
    print(fname)

b1 = tk.Button(window, text= 'Select folder', command = 
               lambda:select_folder(folder_name_tk))
b1.pack()

folder_name_tk = tk.StringVar()
lb = tk.Label(window,textvariable = folder_name_tk, bg = 'Yellow',width = 200)
lb.pack()


def analyzing(folder_name_tk):
    '''
    folder_name_tk: tk.StringVar()
    function: init data_sets_class and plot graph
    '''
    foldername = folder_name_tk.get()
    data_set = data_sets_class.PV_series_data(foldername)
    print(data_set)
    
b2 = tk.Button(window, text= 'Analyze', 
               command = lambda: analyzing(folder_name_tk))
b2.pack()

window.mainloop()