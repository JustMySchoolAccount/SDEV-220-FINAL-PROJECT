from tkinter import *
import tkinter as tk
from pandas import *
import pandas as pd
def button_clicked():
    print("Button Clicked!")

class MenuButton():
        
    def __init__(self, action : str, root : Tk):
        self.BUTTON_WIDTH = 15
        self.BUTTON_HEIGHT = 3
        self.transactionTotal = 0.0
        self.transactionName = []
        self.transactionNums = []

        self.mainFrameMenu = tk.Frame(root)
        self.mainFrameMenu.config(background='#808080')
        self.sideFrameWindow = tk.Frame(root)
        self.sideFrameWindow.config(background='#808080')
        self.controlFrameWindow = tk.Frame(root)
        self.controlFrameWindow.config(background='#808080')

        self.mainFrameMenu.place(x=500, y=50)
        self.button1 = tk.Button(self.mainFrameMenu, text="Pizza: Custom", command=self.loadPizza, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button1.grid(row=0, column=0, pady=10)
        self.button2 = tk.Button(self.mainFrameMenu, text="Pizza: Specialty", command=self.loadSpecialty, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button2.grid(row=1, column=0, pady=10)
        self.button3 = tk.Button(self.mainFrameMenu, text="Pasta", command=self.loadPasta, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button3.grid(row=2, column=0, pady=10)
        self.button4 = tk.Button(self.mainFrameMenu, text="Cheese Steaks", command=self.loadCheese, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button4.grid(row=3, column=0, pady=10)
        self.button5 = tk.Button(self.mainFrameMenu, text="Hoagie", command=self.loadHoagie, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button5.grid(row=4, column=0, pady=10)
        self.button6 = tk.Button(self.mainFrameMenu, text="Drinks", command=self.loadDrinks, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button6.grid(row=6, column=0, pady=10)
        self.button7 = tk.Button(self.mainFrameMenu, text="Extras", command=self.loadExtras, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button7.grid(row=7, column=0, pady=10)
        self.button8 = tk.Button(self.mainFrameMenu, text="COMPLETE", command=self.completeTransaction, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button8.grid(row=8, column=0, pady=10)

        #setting up the total counter widget
        self.desc = Text(self.controlFrameWindow, height=30, width=50)
        self.totals = Text(self.controlFrameWindow, height=3, width=50, background='#72a3f2')
        self.desc.pack()
        self.totals.pack()
        self.totals.insert(tk.END, "Total: ")
        self.desc.insert(tk.END, "DESCRIPTION                        COST\n")
        self.controlFrameWindow.place(x=75, y=55)
        
    def clearFoodMenu(self):
        for widget in self.sideFrameWindow.winfo_children():
            widget.destroy()
    
    #I just realized I could abstract all of these into a single function with a rework, but I just need points at this point because its 6am..
    def loadPizza(self):
        self.clearFoodMenu()
        self.calculatePrice('Cheese Pizza', 10.99)
        index = 0
        buttonList = []
        index = 0
        items = ['Extra Cheese', 'Extra Sauce','Pepperoni', 'Sausage', 'Mushroom', 'Hot Honey', 'Parmesan', 'Basil', 'anchovies']
        prices = [1.93, 0.99, 1.49, 2.25, 1.49, 0.99, 0.99, 0.99, 1.75]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)

    def loadSpecialty(self):
        self.clearFoodMenu()
        index = 0
        items = ['Philly', 'Masterpiece','Vegetarian', 'Hawaiin', '5-Cheese', 'Mona Lisa', 'Spicy Leonardo', 'Double Pepperoni', 'Tropical Heat', 'Sweet&Spicy', 'Chicken Cordon Bleu']
        prices = [10.99, 12.99, 7.99, 9.99, 8.99, 11.99, 11.99, 11.99, 10.99, 13.99, 14.99]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)
    
    def loadPasta(self):
        self.clearFoodMenu()
        index = 0
        items = ['Lasagna Rollups', 'Marinara', 'Alfredo', 'Creamy Tomato', 'Chili Mac', 'Chicken Alfredo', 'Family Alfredo', 'Family Marinara', 'Family Chicken', 'F Creamy Tomato']
        prices = [10.99, 12.99, 7.99, 9.99, 8.99, 11.99, 11.99, 13.99, 13.99, 13.99]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)

    def loadCheese(self):
        self.clearFoodMenu()
        index = 0
        items = ['Beef&Cheese', 'Chickn&Cheese', 'Chickn&Pastromi', 'Beef&Chicken', 'Beef&Pastromi','Chicken&Pepperoni', 'Beef&Pepperoni', 'Chickn&Beef&Chs', 'Veggie Cheese']
        prices = [11.99, 11.99, 11.99, 11.99, 11.99, 11.99, 11.99, 11.99, 11.99]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)
    
    def loadHoagie(self):
        self.clearFoodMenu()
        index = 0
        items = ['Ham','Vegetarian',"4-cheese",'Turkey','Combo','Italian','Turkey Bacon','Club','Meatball','Pizza','Salami','Pastrami','BLT','Tuna']
        prices = [10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99,]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)
    
    def loadDrinks(self):
        self.clearFoodMenu()
        index = 0
        items = ['Pepsi','Mountain Dew','Diet Pepsi','Starry','Dr. Pepper','Lemonade','Cherry Pepsi','Brisk Raspberry','Iced Tea',"mtn-dew diet",'Root Beer','Diet drpepper', 'Fruit Punch']
        prices = [2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99, 2.99,]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)

    def loadExtras(self):
        self.clearFoodMenu()
        index = 0
        items = ['Garlic Bread', 'Cookies', 'Ranch', 'Marinara', 'Alfredo', 'French Fries','Potato Chips']
        prices = [4.99, .99, .99, .99, .99, 3.99, 1.50]
        buttons = {}
        for i, lang in enumerate(items):
            price = prices[i]
            buttons[lang] = Button(self.sideFrameWindow, text=lang, command=lambda name=lang, p = price: self.calculatePrice(name, p), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
            buttons[lang].grid(row=int(index/2), column=index%2, padx=10, pady=10)
            index = index + 1
        self.sideFrameWindow.place(x=650, y=50)

    def calculatePrice(self, name, cost):
        self.transactionName.insert(0, name)
        self.transactionNums.insert(0, cost)
        self.printTransaction()

    def printTransaction(self):
        text = self.transactionName[0]
        text = text.upper()
        numValue = str(self.transactionNums[0])
        spacer = "                       "
        endline = '\n'
        tempLine =text + spacer + numValue + endline
        self.desc.insert(tk.END, tempLine)
        total = 'Total:                       '
        totalCost = str(self.runTotal())
        total = total + totalCost
        self.totals.delete("1.0", "end")
        self.totals.insert(tk.END, total)


    def runTotal(self):
        total = 0
        for num in self.transactionNums:
            total = total + num
        return total

    def completeTransaction(self):
        data = {'Name': self.transactionName, 'Cost':self.transactionNums}
        df = pd.DataFrame(data)
        df.to_excel('output.xlsx', index=False)
        self.totals.delete("1.0", "end")
        self.desc.delete("1.0", "end")
        self.totals.insert(tk.END, "Total: ")
        self.desc.insert(tk.END, "DESCRIPTION                        COST\n")