import os
import time
import sys
import tkinter as tk

root = tk.Tk()

root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(2,weight=1)

#Display settings
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, borderwidth=5, justify="center")
display.grid(row=1,column=0, columnspan=5,sticky="ew", padx=0, pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=2, column=0, columnspan=5,sticky="nsew", padx=5, pady=5) 


#Attributing weights to the rows and column so the behave dynamic 
for i in range(5):
    buttons_frame.grid_columnconfigure(i, weight=1)

for i in range(7):
    buttons_frame.grid_rowconfigure(i, weight=1)


#Functions
def insert_number_on_display(value):
    display_var.set(display_var.get() + str(value))


def clean_display():
    display_var.set("")

def calculate_result():
    try:
        result= str(eval(display_var.get()))
        display_var.set(result)
    
    except:
        display_var.set("Error!")
#Buttons of numbers 
btn_7 = tk.Button(buttons_frame, text="7", command=lambda: insert_number_on_display("7"))
btn_7.grid(row=3, column=0,sticky="nsew", padx=3, pady=3)
btn_8 = tk.Button(buttons_frame, text="8",  command=lambda: insert_number_on_display("8") )
btn_8.grid(row=3, column=1,sticky="nsew", padx=3, pady=3)
btn_9 = tk.Button(buttons_frame, text="9",  command=lambda: insert_number_on_display("9") )
btn_9.grid(row=3, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_4 = tk.Button(buttons_frame, text="4", command=lambda: insert_number_on_display("4") )
btn_4.grid(row=4, column=0,sticky="nsew", padx=3, pady=3)
btn_5 = tk.Button(buttons_frame, text="5",  command=lambda: insert_number_on_display("5") )
btn_5.grid(row=4, column=1,sticky="nsew", padx=3, pady=3)
btn_6 = tk.Button(buttons_frame, text="6", command=lambda: insert_number_on_display("6") )
btn_6.grid(row=4, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_1 = tk.Button(buttons_frame, text="1", command=lambda: insert_number_on_display("1") )
btn_1.grid(row=5, column=0,sticky="nsew", padx=3, pady=3)
btn_2 = tk.Button(buttons_frame, text="2", command=lambda: insert_number_on_display("2") )
btn_2.grid(row=5, column=1,sticky="nsew", padx=3, pady=3)
btn_3 = tk.Button(buttons_frame, text="3", command=lambda: insert_number_on_display("3") )
btn_3.grid(row=5, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_0 = tk.Button(buttons_frame, text="0", command=lambda: insert_number_on_display("0") )
btn_0.grid(row=6, column=0,sticky="nsew", padx=3, pady=3)

#Buttons of signs 
btn_div = tk.Button(buttons_frame, text="/", command=lambda: insert_number_on_display("/"))
btn_div.grid(row=3, column=3,sticky="nsew", padx=3, pady=3)
btn_mul = tk.Button(buttons_frame, text="x", command=lambda: insert_number_on_display("*") )
btn_mul.grid(row=4, column=3,sticky="nsew", padx=3, pady=3)
btn_sub = tk.Button(buttons_frame, text="-", command=lambda: insert_number_on_display("-") )
btn_sub.grid(row=5, column=3,sticky="nsew", padx=3, pady=3)
btn_add = tk.Button(buttons_frame, text="+", command=lambda: insert_number_on_display("+") )
btn_add.grid(row=6, column=3,sticky="nsew", padx=3, pady=3)
btn_eq = tk.Button(buttons_frame, text="=", command=lambda: calculate_result())
btn_eq.grid(row=6, column=2,sticky="nsew", padx=3, pady=3)
btn_dot = tk.Button(buttons_frame, text=".", command=lambda: insert_number_on_display(".") )
btn_dot.grid(row=6, column=1,sticky="nsew", padx=3, pady=3)
btn_clear = tk.Button(buttons_frame, text="C", command=lambda: clean_display())
btn_clear.grid(row=3, column=4,sticky="nsew", padx=3, pady=3)



if __name__ == "__main__":

 
    root.mainloop()

