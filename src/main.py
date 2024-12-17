from tkinter import *
import tkinter as tk
from mainWindow import MenuButton

"""
At this point, my POS system has been heavily reduced in total functionality. its current functionality is this:

display and track current ticket, allow user to input different menu items, and have the total be displayed in the bottom. 

Once transaction is completed, data is stored in a CSV file, when the program is exited, an Excel spreadsheet will be generated with the infor
"""
def onClosing():
    print("test!")
    root.destroy()

global root

root = tk.Tk()
root.resizable(False,False)
root.geometry('1000x720')

root.config(bg='#808080')

test = MenuButton("Test", root)
root.protocol("WM_DELETE_WINDOW", onClosing)
root.mainloop()