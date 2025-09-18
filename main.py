import os
import time
import sys
import tkinter as tk
import requests


class CalculatorInterface:
    def __init__(self):     
        #Iniiating the root window and setting attributes
        self.engine = CalculatorEngine() 
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
        if event.char in "0123456789":
            self.insert_number_on_display(event.char)
        elif event.char in "+-*/":
            last_value = self.engine.expression[-1]
            if last_value in "+-*/":
                return 0
            else:
                self.insert_number_on_display(event.char)

        elif event.keysym=="Return":
            self.calculate_result()
        elif event.keysym=="BackSpace":
            self.erase_values()

    def run(self):
        self.root.mainloop()
 

    def insert_number_on_display(self,value):
        self.display.configure(state="normal")
        self.engine.insert(value)
        self.display_var.set(self.engine.expression)
        self.display.configure(state="readonly")

    def clean_display(self):
        self.display.configure(state="normal")
        self.engine.clean()
        self.display_var.set("")
        self.display.configure(state='readonly')# Doesn't let the user edit the values directly on the display

    def calculate_result(self):
        try:
            self.display.configure(state="normal")
            result= self.engine.calculate()
            self.display_var.set(result)
            self.display.configure(state="readonly")

        except:
            
            self.display_var.set("Error!")
            

    def erase_values(self):
        self.display.configure(state="normal")
        self.engine.clean()
        self.display_var.set(self.engine.expression) #Erases the last characterer inserted
        self.display.configure(state="readonly")

    def create_buttons(self):
        buttons = [
            ("Convert", 1, 0, 4, lambda: self.create_popup_window()),
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

    def create_popup_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Conversion")
        w, h = 250, 350


        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        new_window_x = root_x + (root_width // 2 - w // 2)
        new_window_y = root_y + (root_height // 2 - h // 2)

        self.new_window.geometry(f"{w}x{h}+{new_window_x}+{new_window_y}")
        self.new_window.resizable(False, False)
        self.new_window.attributes("-toolwindow", True)
        self.new_window.transient(self.root)
        self.new_window.grab_set()

class CalculatorEngine:
    def __init__(self):
        self.expression= ""
    
    def insert(self, value: str):
        self.expression += str(value)
    
    def clean(self):
        self.expression = self.expression[:-1]
    
    def erase(self):
        self.expression = self.expression[:-1]
    
    def calculate(self):
        try:
            result= eval(self.expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            else:
                self.expression = str(result)

            return self.expression

        
        except Exception:
            self.expression = ""
            return "Error"

class CurrencyConverter:
    def __init__(self):
        self.access_key="68841c785c60466b1669198d"
        
        

    def convert(self,from_currency: str, to_currency: str, amount: float) -> float:
        url = f"https://v6.exchangerate-api.com/v6/{self.access_key}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()
        
        if data["result"] == "success":
            return data["conversion_result"]
        
        else:
            raise Exception(f"Conversion error: {data['error-type']}")



if __name__ == "__main__":
    calculator = CalculatorInterface()
    calculator.run()