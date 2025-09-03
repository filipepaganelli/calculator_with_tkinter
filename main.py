import os
import time
import sys
import tkinter as tk

root = tk.Tk()

root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, width=20, borderwidth=5, justify="right")
display.grid(row=1,column=0, columnspan=4, padx=5, pady=5)




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
btn_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: insert_number_on_display("7"))
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: insert_number_on_display("8") )
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: insert_number_on_display("9") )
btn_9.grid(row=3, column=2)

#Buttons of numbers 
btn_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: insert_number_on_display("4") )
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: insert_number_on_display("5") )
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: insert_number_on_display("6") )
btn_6.grid(row=4, column=2)

#Buttons of numbers 
btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: insert_number_on_display("1") )
btn_1.grid(row=5, column=0)
btn_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: insert_number_on_display("2") )
btn_2.grid(row=5, column=1)
btn_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: insert_number_on_display("3") )
btn_3.grid(row=5, column=2)

#Buttons of numbers 
btn_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: insert_number_on_display("0") )
btn_0.grid(row=6, column=0)

#Buttons of signs 
btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda: insert_number_on_display("/"))
btn_div.grid(row=3, column=3)
btn_mul = tk.Button(root, text="x", width=5, height=2, command=lambda: insert_number_on_display("*") )
btn_mul.grid(row=4, column=3)
btn_sub = tk.Button(root, text="-", width=5, height=2, command=lambda: insert_number_on_display("-") )
btn_sub.grid(row=5, column=3)
btn_add = tk.Button(root, text="+", width=5, height=2, command=lambda: insert_number_on_display("+") )
btn_add.grid(row=6, column=3)
btn_eq = tk.Button(root, text="=", width=5, height=2, command=lambda: calculate_result())
btn_eq.grid(row=6, column=2)
btn_dot = tk.Button(root, text=".", width=5, height=2, command=lambda: insert_number_on_display(".") )
btn_dot.grid(row=6, column=1)
btn_clear = tk.Button(root, text="C", width=5, height=2, command=lambda: clean_display())
btn_clear.grid(row=3, column=4)



if __name__ == "__main__":

 
    root.mainloop()

