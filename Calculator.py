from tkinter import *


calculator = Tk()     # This creates a window
calculator.title("Calculator")
#calculator.geometry("700x500")

large_font = ('Verdana',30)

cal_entry = Entry(calculator, width=20, font=large_font, borderwidth = 5)
cal_entry.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 10)
#cal_entry.insert(0, "Enter Value: ")

num1_global = 0
num2_global = 0
operation = ''
oper = ''
total_final = 0


def addition():
    global num1_global
    global operation
    global oper
    oper = ""
    operation = "addition"
    num1 = int(cal_entry.get())
    num1_global = num1
    cal_entry.delete(0,END)
    return


def subtraction():
    global num1_global
    global operation
    global oper
    oper = ""
    operation = "subtraction"
    num1 = int(cal_entry.get())
    num1_global = num1
    cal_entry.delete(0, END)
    return


def multiplication():
    global num1_global
    global operation
    global oper
    oper = ""
    operation = "multiplication"
    num1 = int(cal_entry.get())
    num1_global = num1
    cal_entry.delete(0,END)
    return


def division():
    global num1_global
    global operation
    global oper
    oper = ""
    operation = "division"
    num1 = int(cal_entry.get())
    num1_global = num1
    cal_entry.delete(0,END)
    return


def percentage():
    global num1_global
    global operation
    global oper
    oper = ""
    operation = "percentage"
    num1 = int(cal_entry.get())
    num1_global = num1
    cal_entry.delete(0,END)
    return


def button_click(number):
    ent = cal_entry.get()
    cal_entry.delete(0,END)
    cal_entry.insert(0,(str(ent)+str(number)))
    ent = int(number)
    return


def back():
    cal_entry.delete(0)
    return


def clear():
    global num1_global
    num1_global = 0
    global num2_global
    num2_global = 0
    global total_final
    total_final = 0
    global operation
    operation = "equal"
    cal_entry.delete(0,END)



def button_total():
    global num1_global
    global num2_global
    global total_final
    global operation
    global oper
    num1 = num1_global
    print(num1)

    if (oper == ""):
        num2 = int(cal_entry.get())
        num2_global = num2
    else:
        num2 = num2_global


    if ((operation == "division") and (int(num2) == 0)):
        cal_entry.delete(0,END)
        cal_entry.insert(0, "Division by 0")
    else:
        operations = {
            "addition": (int(num1) + int(num2)),
            "subtraction": (int(num1)  - int(num2)),
            "multiplication": (int(num1)  * int(num2)),
            "division": ((int(num1))/(int(num2))),
            "percentage": (((int(num1)) / 100) * (int(num2))),
            "equal": 0
        }


        total_final = int(operations.get(operation))
        cal_entry.delete(0,END)
        cal_entry.insert(0,total_final)
        oper = "equal"
        num1_global = total_final
        print("num1: ",num1," num2: ", num2," num1 global: ", num1_global," total_final: ",total_final)
        print("num2_global: ", num2_global)
    return




# Creating Labels for the calculator

'''
add_label = Label (calculator, text ="Addition").grid(row=1, column = 0)
subtract_label = Label (calculator, text ="Subtraction").grid(row=2, column = 0)
multiply_label = Label (calculator, text ="Multiply").grid(row=3, column = 0)
divide_label = Label (calculator, text ="Divide").grid(row=4, column = 0)
percentage_label = Label (calculator, text ="Percentage").grid(row=5, column = 0)
'''

# Define top row functions
button_clear= Button(calculator, text="CLEAR", padx=22, pady=20, command=clear)
button_back= Button(calculator, text="BACK", padx=25, pady=20, command=back)
button_clear.grid(row=1, column = 0)
button_back.grid(row=1, column = 1)

# Define Number buttons
button_1 = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_period = Button(calculator, text=".", padx=40, pady=20, state=DISABLED, command=lambda: button_click())
button_0 = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_equal = Button(calculator, text="=", padx=40, pady=20, command=button_total)

# Define Button grid
button_7.grid(row=2, column = 0)
button_8.grid(row=2, column = 1)
button_9.grid(row=2, column = 2)

button_4.grid(row=3, column = 0)
button_5.grid(row=3, column = 1)
button_6.grid(row=3, column = 2)

button_1.grid(row=4, column = 0)
button_2.grid(row=4, column = 1)
button_3.grid(row=4, column = 2)

button_period.grid(row=5, column = 0)
button_0.grid(row=5, column = 1)
button_equal.grid(row=5, column = 2)

#Define Function Buttons
button_add = Button(calculator, text =" +  ", padx=41, pady=20, command = addition)
button_subtract = Button(calculator, text ="  -  ", padx=40, pady=20, command = subtraction)
button_multiply = Button(calculator, text ="  X  ", padx=40, pady=20, command = multiplication)
button_divide = Button(calculator, text ="  /  ", padx=42, pady=20, command = division)
button_percent = Button(calculator, text ="  %  ", padx=40, pady=20, command = percentage, state=DISABLED)

#Define Function Buttons GRID
button_add.grid(row=1, column = 4)
button_subtract.grid(row=2, column = 4)
button_multiply.grid(row=3, column = 4)
button_divide.grid(row=4, column = 4)
button_percent.grid(row=5, column = 4)




calculator.mainloop()
