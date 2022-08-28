from operator import eq
from tkinter import *
import tkinter

equation_string = ""
current_number = ""
num_is_percentage = False;

def add_number(num):
    global current_number
    if current_number == "" and num == 0 or num_is_percentage:
        return
    else:
        current_number += str(num)
        equation_display.config(text=current_number)

def add_operator(op):
    global equation_string
    global current_number
    global num_is_percentage
    if equation_display == "0":
        return
    else:
        if op == "/":
            equation_display.config(text="÷")
        elif op == "*":
            equation_display.config(text="×")
        else:
            equation_display.config(text=op)
        equation_string += current_number + " " + op + " "
        current_number = ""
        num_is_percentage = False

def add_decimal():
    global equation_string
    global current_number
    if current_number.__contains__("."):
        return
    else:
        if current_number == "":
            equation_string += "0."
            current_number += "0."
        else:
            equation_string += "."
            current_number += "."
        equation_display.config(text=current_number)

def cancel():
    global equation_string
    global current_number
    equation_string = ""
    current_number = ""
    equation_display.config(text="0")

def equals():
    global equation_string
    global current_number
    if equation_string == current_number:
        equation_display.config(text=current_number)
    else:
        equation_string += current_number
        equation_display.config(text=str(eval(equation_string)))
    print(equation_string)
    equation_string = str(eval(equation_string))
    current_number = ""

def percentage():
    global current_number
    global num_is_percentage
    current_number = str(int(current_number) / 100)
    equation_display.config(text=current_number)
    num_is_percentage = True

def switch_positive_negative():
    global current_number
    if current_number == "":
        return
    else:
        current_number = str(int(current_number) * -1)
        equation_display.config(text=current_number)


root = Tk()
root.geometry("360x480")
root.title("Calculator")

display_frame = Frame(root, bg="#5c5858")
display_frame.pack(fill="both", expand=True)

button_frame = Frame(root, bg="#424040")
button_frame.pack(fill="both", expand=True, ipady=60)

display_frame.rowconfigure(0, weight=1)
display_frame.columnconfigure(0, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

equation_display = Label(display_frame, text="0", font=("Arial 50"), anchor=E, padx=25)
equation_display.grid(row=0, column=0, columnspan=4, sticky=tkinter.NSEW)

num_1 = Button(button_frame, text="1", font=("Arial 25"), command=lambda:add_number(1))
num_1.grid(row=3, column=0, sticky=tkinter.NSEW)
num_2 = Button(button_frame, text="2", font=("Arial 25"), command=lambda:add_number(2))
num_2.grid(row=3, column=1, sticky=tkinter.NSEW)
num_3 = Button(button_frame, text="3", font=("Arial 25"), command=lambda:add_number(3))
num_3.grid(row=3, column=2, sticky=tkinter.NSEW)
btn_add = Button(button_frame, text="+", font=("Arial 25"), command=lambda:add_operator("+"))
btn_add.grid(row=3, column=3, sticky=tkinter.NSEW)

num_4 = Button(button_frame, text="4", font=("Arial 25"), command=lambda:add_number(4))
num_4.grid(row=2, column=0, sticky=tkinter.NSEW)
num_5 = Button(button_frame, text="5", font=("Arial 25"), command=lambda:add_number(5))
num_5.grid(row=2, column=1, sticky=tkinter.NSEW)
num_6 = Button(button_frame, text="6", font=("Arial 25"), command=lambda:add_number(6))
num_6.grid(row=2, column=2, sticky=tkinter.NSEW)
btn_subtract = Button(button_frame, text="-", font=("Arial 25"), command=lambda:add_operator("-"))
btn_subtract.grid(row=2, column=3, sticky=tkinter.NSEW)

num_7 = Button(button_frame, text="7", font=("Arial 25"), command=lambda:add_number(7))
num_7.grid(row=1, column=0, sticky=tkinter.NSEW)
num_8 = Button(button_frame, text="8", font=("Arial 25"), command=lambda:add_number(8))
num_8.grid(row=1, column=1, sticky=tkinter.NSEW)
num_9 = Button(button_frame, text="9", font=("Arial 25"), command=lambda:add_number(9))
num_9.grid(row=1, column=2, sticky=tkinter.NSEW)
btn_multiply = Button(button_frame, font=("Arial 25"), text="×", command=lambda:add_operator("*"))
btn_multiply.grid(row=1, column=3, sticky=tkinter.NSEW)

btn_cancel = Button(button_frame, text="C", font=("Arial 25"), command=cancel)
btn_cancel.grid(row=0, column=0, sticky=tkinter.NSEW)
btn_positive_negative = Button(button_frame, text="+/-", font=("Arial 25"), command=switch_positive_negative)
btn_positive_negative.grid(row=0, column=1, sticky=tkinter.NSEW)
btn_percent = Button(button_frame, text="%", font=("Arial 25"), command=percentage)
btn_percent.grid(row=0, column=2, sticky=tkinter.NSEW)
btn_divide = Button(button_frame, text="÷", font=("Arial 25"), command=lambda:add_operator("/"))
btn_divide.grid(row=0, column=3, sticky=tkinter.NSEW)

num_0 = Button(button_frame, text="0", font=("Arial 25"), command=lambda:add_number(0))
num_0.grid(row=4, column=0, columnspan=2,sticky=tkinter.NSEW)
btn_decimal = Button(button_frame, text=".", font=("Arial 25"), command=add_decimal)
btn_decimal.grid(row=4, column=2, sticky=tkinter.NSEW)
btn_equals = Button(button_frame, text="=", font=("Arial 25"), command=equals)
btn_equals.grid(row=4, column=3, sticky=tkinter.NSEW)

root.mainloop()