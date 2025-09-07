import os
import time
import sys
import tkinter as tk


class CalculatorInterface:
    def __init__(self):     
        #Iniiating the root window and setting attributes 
        self.root = tk.Tk()
        self.root.title("Calculator-Paganelli")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.buttons_font = ("Arial", 15) 

        self.create_display()
        self.create_buttons_frame()
        self.configure_layout()
        self.bind_keys()
        self.create_buttons()


    def create_display(self):
        #Display settings
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self.root, 
            textvariable=self.display_var, 
            borderwidth=5, 
            justify="center", 
            font=("Arial", 24), 
            state="readonly")

        self.display.grid(rowspan=2,columnspan=4,sticky="ew", padx=0, pady=5)

    def create_buttons_frame(self):
        #Buttons Frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=2, column=0, columnspan=5,sticky="nsew", padx=5, pady=5) 

        

        #Attributing weights to the rows and column so the behave dynamic 
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

        for i in range(7):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def configure_layout(self): 
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_rowconfigure(2,weight=1)

    def bind_keys(self):    
        self.root.bind("<Key>", self.handle_keypress)

    def handle_keypress(self,event):
        if event.char in "0123456789+-*/":
            self.insert_number_on_display(event.char)
        elif event.keysym=="Return":
            self.calculate_result()
        elif event.keysym=="BackSpace":
            self.erase_values()

    def run(self):
        self.root.mainloop()


    def insert_number_on_display(self,value):
        self.display.configure(state="normal")
        self.display_var.set(self.display_var.get() + str(value))
        self.display.configure(state="readonly")

    def clean_display(self):
        self.display.configure(state="normal")
        self.display_var.set("")
        self.display.configure(state='readonly')# Doesn't let the user edit the values directly on the display

    def calculate_result(self):
        try:
            result= eval(self.display_var.get())
            result = int(result) if isinstance(result, float) and result.is_integer() else result #As the result of eval() always return a float, this code checks if it's integer to format the display value with no d
            result= str(result)
            self.display_var.set(result)
        
        except:
            self.display.configure(state="normal")
            self.display_var.set("Error!")
            self.display.configure(state="readonly")

    def erase_values(self):
        display_values = self.display_var.get()
        self.display_var.set(display_values[:-1]) #Erases the last characterer inserted



    def create_buttons(self):
        buttons = [
            ("C",2,0,4, self.clean_display),
            ("7", 3, 0, 1, lambda: self.insert_number_on_display("7")),
            ("8", 3, 1, 1, lambda: self.insert_number_on_display("8")),
            ("9", 3, 2, 1, lambda: self.insert_number_on_display("9")),
            ("/", 3, 3, 1, lambda: self.insert_number_on_display("/")),
            ("4", 4, 0, 1, lambda: self.insert_number_on_display("4")),
            ("5", 4, 1, 1, lambda: self.insert_number_on_display("5")),
            ("6", 4, 2, 1, lambda: self.insert_number_on_display("6")),
            ("x", 4, 3, 1, lambda: self.insert_number_on_display("*")),
            ("1", 5, 0, 1, lambda: self.insert_number_on_display("1")),
            ("2", 5, 1, 1, lambda: self.insert_number_on_display("2")),
            ("3", 5, 2, 1, lambda: self.insert_number_on_display("3")),
            ("-", 5, 3, 1, lambda: self.insert_number_on_display("-")),
            ("0", 6, 0, 1, lambda: self.insert_number_on_display("0")),
            (".", 6, 1, 1, lambda: self.insert_number_on_display(".")),
            ("=", 6, 2, 1, self.calculate_result),
            ("+", 6, 3, 1, lambda: self.insert_number_on_display("+")),
        ]

        for (text, row, column, columnspan, command) in buttons:
            tk.Button(self.buttons_frame, text=text, font=self.buttons_font, command=command ).grid(row=row, column=column,columnspan=columnspan,sticky="snew", padx=3, pady=3)

       



if __name__ == "__main__":
    calculator = CalculatorInterface()
    calculator.run()