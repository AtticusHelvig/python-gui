from tkinter import *

root = Tk()
root.title("Calculator")

def num_key(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))
    
def operation_key(sign):
    global f_num
    global operation
    num1 = entry.get()
    f_num = int(num1)
    entry.delete(0, END)
    operation = sign
    
def equal_key():
    result = 0
    num2 = entry.get()
    num2 = int(num2)
    
    entry.delete(0, END)
    match operation:
        case "+": result = f_num + num2
        case "-": result = f_num - num2
        case "*": result = f_num * num2
        case "/": result = int(f_num / num2)
    entry.insert(0, str(result))
    
def clear_key():
    global f_num
    global operation
    operation = "+"
    f_num = 0
    entry.delete(0, END)

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

font = "Times"
fg = "#ffffff"
bg = "#15191d"
SHORT_BUTTON_X = 40
SHORT_BUTTON_Y = 20

button0 = Button(root, text=str(0), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(0))
button1 = Button(root, text=str(1), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(1))
button2 = Button(root, text=str(2), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(2))
button3 = Button(root, text=str(3), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(3))
button4 = Button(root, text=str(4), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(4))
button5 = Button(root, text=str(5), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(5))
button6 = Button(root, text=str(6), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(6))
button7 = Button(root, text=str(7), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(7))
button8 = Button(root, text=str(8), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(8))
button9 = Button(root, text=str(9), padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                 bg=bg, fg=fg, font=font, command=lambda: num_key(9))

button_plus = Button(root, text="+", padx=SHORT_BUTTON_X - 1, pady=SHORT_BUTTON_Y, 
                     bg=bg, fg=fg, font=font, command=lambda: operation_key("+"))
button_equal = Button(root, text="=", padx=SHORT_BUTTON_X + 53, pady=SHORT_BUTTON_Y,
                      bg=bg, fg=fg, font=font, command=equal_key)
button_clear = Button(root, text="CLEAR", padx=SHORT_BUTTON_X + 24, pady=SHORT_BUTTON_Y,
                      bg=bg, fg=fg, font=font, command=clear_key)
button_minus = Button(root, text="-", padx=SHORT_BUTTON_X + 2, pady=SHORT_BUTTON_Y, 
                     bg=bg, fg=fg, font=font, command=lambda: operation_key("-"))
button_multiply = Button(root, text="x", padx=SHORT_BUTTON_X, pady=SHORT_BUTTON_Y, 
                     bg=bg, fg=fg, font=font, command=lambda: operation_key("*"))
button_divide = Button(root, text="/", padx=SHORT_BUTTON_X + 3, pady=SHORT_BUTTON_Y, 
                     bg=bg, fg=fg, font=font, command=lambda: operation_key("/"))

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()