# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:08:12 2018

@author: ustci
"""

import tkinter as tk
import data_sets_class

#import tkinter.filedialog
# import tkinter.messagebox
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def select_folder():
    fname = tk.filedialog.askdirectory()
    if fname:
        try:
            print("""here it comes: self.settings["template"].set(fname)""")
        except:                     # <- naked except is a bad idea
            tk.messagebox.showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    print(fname)
    folder_name.set(fname)

b1 = tk.Button(window, text= 'Select folder', command = select_folder)
b1.pack()

folder_name = tk.StringVar()
lb = tk.Label(window,textvariable = folder_name, bg = 'Yellow',width = 200)
lb.pack()

def analyzing(folder_name):
    
    
b2 = tk.Button(window, text= 'Analyze', command = analyzing(folder_name))
b2.pack()

window.mainloop()