# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:08:12 2018

@author: ustci

Todolist:
    - select folder (done!)
    - enter the label (done!)
    - make exe (on-going)
    - plot the graph in window
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

label_input = tk.Text(window,height = 2)
label_input.pack()


def input_labels(label_input,grouplb_tk):
    '''
    
    '''
    grouplb_tk.set(label_input.get("1.0",'end-1c'))
    

b3 = tk.Button(window, text= 'Input group labels(sep by:/)', 
               command = lambda: input_labels(label_input,grouplb_tk))
b3.pack()

grouplb_tk = tk.StringVar()
lb_grouplb = tk.Label(window,textvariable = grouplb_tk, bg = 'Green',width = 200)
lb_grouplb.pack()

def analyzing(folder_name_tk,grouplb_tk):
    '''
    folder_name_tk: tk.StringVar()
    grouplb_tk:
    function: init data_sets_class and plot graph
    '''
    foldername = folder_name_tk.get()
    group_label = grouplb_tk.get().split('/')
    print(group_label)
    data_set = data_sets_class.PV_series_data(foldername)
    data_set.sort(group_label)
    print(data_set)
    data_set.get_boxplot()
    
    
b2 = tk.Button(window, text= 'Analyze', 
               command = lambda: analyzing(folder_name_tk,grouplb_tk))
b2.pack()

window.mainloop()