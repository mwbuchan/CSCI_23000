''' BMI Calculator
    Created by Maggie Buchanan
    CSCI 23000
    11/13/15'''
#[weight /  (height)]**2 * 703

from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.headerFont = ("Comic", "16", "bold")

        self.title("BMI Calculator")
        self.addInput()
        self.addOutput()

    def addInput(self):
        '''height and weight is received from user'''
        
        Label(self, text = "Calculate your BMI!",
              font = self.headerFont).grid(columnspan = 2, padx = 5)
        
        Label(self, text = "Height").grid(row = 1, column = 0, padx = 5)
        self.txtHeight = Entry(self)
        self.txtHeight.grid(row = 1, column = 1, padx = 5)
        self.txtHeight.insert(0, "inches")
                               
        
        Label(self, text = "Weight").grid(row = 2, column = 0, padx = 5)
        self.txtWeight = Entry(self)
        self.txtWeight.grid(row = 2, column = 1, padx = 5)
        self.txtWeight.insert(0, "pounds")

    def addOutput(self):
        '''add button and output labels'''
        
        self.lblBMI = Label(self, text = "Body Mass Index")
        self.lblBMI.grid(row = 4, column = 0)
        self.lblResult = Label(self, text = "Weight Group")
        self.lblResult.grid(row = 5, column = 0)

        self.btnCalc = Button(self, text = "Calculate!")
        self.btnCalc.grid(row = 3, column = 0)
        self.btnCalc["command"] = self.getBMI

        self.btnReset = Button(self, text = "Reset")
        self.btnReset.grid(row = 3, column = 1)
        self.btnReset["command"] = self.reset

        self.txtBMI = Entry(self)
        self.txtBMI.grid(row = 4, column = 1)
        self.txtBMI.insert(0, "")
                         
        self.txtResult = Entry(self)
        self.txtResult.grid(row = 5, column = 1)
        self.txtResult.insert(0, "")
        
    def getBMI(self):
        '''height and weight are used to calculate BMI'''



        weight = int(self.txtWeight.get())
        height = int(self.txtHeight.get())

        BMI = (weight*703 /  height**2)
        #BMI = round(BMI, 2)
        
        keepGoing = True

        
        while keepGoing:
            if BMI <= 18.5:
                result = "underweight"
                keepGoing = False
            elif BMI == 18.5 or BMI <= 24.9:
                result = "normal"
                keepGoing = False
            elif BMI >= 25 or BMI <= 29.9:
                result = "overweight"
                keepGoing = False
            elif BMI >= 30:
                result = "overweight"
                keepGoing = False

        self.txtBMI.insert(0, str(BMI))
        self.txtResult.insert(0, str(result))
        
    def reset(self):
        '''clear all text entries'''
        self.txtHeight.delete(0, END)
        self.txtWeight.delete(0, END)
        self.txtBMI.delete(0, END)
        self.txtResult.delete(0, END)
        
        self.txtHeight.insert(0, "inches")
        self.txtWeight.insert(0, "pounds")
        self.txtBMI.insert(0, "")
        self.txtResult.insert(0, "")
        
    def main():
        app = App()
        app.mainloop()

App()
