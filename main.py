import os
import time
import sys
import tkinter as tk

#Iniiating the root window and setting attributes 
root = tk.Tk()
root.title("Calculator-Paganelli")
root.geometry("300x400")
root.resizable(False, False)
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(2,weight=1)



#Display settings
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, borderwidth=5, justify="center", font=("Arial", 24), state="readonly")
display.grid(rowspan=2,columnspan=4,sticky="ew", padx=0, pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=2, column=0, columnspan=5,sticky="nsew", padx=5, pady=5) 

buttons_font = ("Arial", 15) 

#Attributing weights to the rows and column so the behave dynamic 
for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)

for i in range(7):
    buttons_frame.grid_rowconfigure(i, weight=1)


#Functions
#
def insert_number_on_display(value):
    display.configure(state="normal")
    display_var.set(display_var.get() + str(value))
    display.configure(state="readonly")

def clean_display():
    display.configure(state="normal")
    display_var.set("")
    display.configure(state='readonly')# Doesn't let the user edit the values directly on the display

def calculate_result():
    try:
        result= eval(display_var.get())
        result = int(result) if isinstance(result, float) and result.is_integer() else result #As the result of eval() always return a float, this code checks if it's integer to format the display value with no d
        result= str(result)
        display_var.set(result)
    
    except:
        display.configure(state="normal")
        display_var.set("Error!")
        display.configure(state="readonly")

def erase_values():
    display_values = display_var.get()
    display_var.set(display_values[:-1]) #Erases the last characterer inserted




def handle_keypress(event):
    
    if event.char in "0123456789+-*/":
        insert_number_on_display(event.char)
    elif event.keysym=="Return":
        calculate_result()
    elif event.keysym=="BackSpace":
        erase_values()




root.bind("<Key>", handle_keypress)





#Creating buttons
#Buttons of numbers 
btn_7 = tk.Button(buttons_frame, text="7",font=buttons_font, command=lambda: insert_number_on_display("7"))
btn_7.grid(row=3, column=0,sticky="nsew", padx=3, pady=3)
btn_8 = tk.Button(buttons_frame, text="8",font=buttons_font,  command=lambda: insert_number_on_display("8") )
btn_8.grid(row=3, column=1,sticky="nsew", padx=3, pady=3)
btn_9 = tk.Button(buttons_frame, text="9",font=buttons_font,  command=lambda: insert_number_on_display("9") )
btn_9.grid(row=3, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_4 = tk.Button(buttons_frame, text="4",font=buttons_font, command=lambda: insert_number_on_display("4") )
btn_4.grid(row=4, column=0,sticky="nsew", padx=3, pady=3)
btn_5 = tk.Button(buttons_frame, text="5",font=buttons_font,  command=lambda: insert_number_on_display("5") )
btn_5.grid(row=4, column=1,sticky="nsew", padx=3, pady=3)
btn_6 = tk.Button(buttons_frame, text="6",font=buttons_font, command=lambda: insert_number_on_display("6") )
btn_6.grid(row=4, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_1 = tk.Button(buttons_frame, text="1",font=buttons_font, command=lambda: insert_number_on_display("1") )
btn_1.grid(row=5, column=0,sticky="nsew", padx=3, pady=3)
btn_2 = tk.Button(buttons_frame, text="2",font=buttons_font, command=lambda: insert_number_on_display("2") )
btn_2.grid(row=5, column=1,sticky="nsew", padx=3, pady=3)
btn_3 = tk.Button(buttons_frame, text="3",font=buttons_font, command=lambda: insert_number_on_display("3") )
btn_3.grid(row=5, column=2,sticky="nsew", padx=3, pady=3)

#Buttons of numbers 
btn_0 = tk.Button(buttons_frame, text="0",font=buttons_font, command=lambda: insert_number_on_display("0") )
btn_0.grid(row=6, column=0,sticky="nsew", padx=3, pady=3)

#Buttons of signs 
btn_div = tk.Button(buttons_frame, text="/",font=buttons_font, command=lambda: insert_number_on_display("/"))
btn_div.grid(row=3, column=3,sticky="nsew", padx=3, pady=3)
btn_mul = tk.Button(buttons_frame, text="x",font=buttons_font, command=lambda: insert_number_on_display("*") )
btn_mul.grid(row=4, column=3,sticky="nsew", padx=3, pady=3)
btn_sub = tk.Button(buttons_frame, text="-",font=buttons_font, command=lambda: insert_number_on_display("-") )
btn_sub.grid(row=5, column=3,sticky="nsew", padx=3, pady=3)
btn_add = tk.Button(buttons_frame, text="+",font=buttons_font, command=lambda: insert_number_on_display("+") )
btn_add.grid(row=6, column=3,sticky="nsew", padx=3, pady=3)
btn_eq = tk.Button(buttons_frame, text="=",font=buttons_font, command=lambda: calculate_result())
btn_eq.grid(row=6, column=2,sticky="nsew", padx=3, pady=3)
btn_dot = tk.Button(buttons_frame, text=".",font=buttons_font, command=lambda: insert_number_on_display(".") )
btn_dot.grid(row=6, column=1,sticky="nsew", padx=3, pady=3)
btn_clear = tk.Button(buttons_frame, text="C",font=buttons_font, command=lambda: clean_display())
btn_clear.grid(row=2, columnspan=4,sticky="nsew", padx=3, pady=3)



if __name__ == "__main__":

 
    root.mainloop()

