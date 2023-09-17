import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

END = 100

root = customtkinter.CTk()
root.geometry("400x500")
root.title("Calculator")

def num_key(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))
    
def operation_key(sign):
    global f_num
    global operation
    num1 = display.get()
    f_num = float(num1)
    display.delete(0, END)
    operation = sign
    
def equal_key():
    result = 0
    num2 = display.get()
    num2 = float(num2)
    
    display.delete(0, END)
    match operation:
        case "+": result = f_num + num2
        case "-": result = f_num - num2
        case "*": result = f_num * num2
        case "/": result = f_num / num2
    display.insert(0, str(result))
    
def clear_key():
    global f_num
    global operation
    operation = "+"
    f_num = 0
    display.delete(0, END)
    
frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

display = customtkinter.CTkEntry(frame, width=280, height=56, font=("Consolas", 24))
display.pack(pady=20)

button_frame = customtkinter.CTkFrame(frame)
button_frame.pack()

button_font = ("Consolas", 48)
button_size = 60

button7 = customtkinter.CTkButton(button_frame, button_size, button_size, text="7", font=button_font, command=lambda: num_key(7))
button7.grid(row=0, column=0, padx=10, pady=10)
button8 = customtkinter.CTkButton(button_frame, button_size, button_size, text="8", font=button_font, command=lambda: num_key(8))
button8.grid(row=0, column=1, padx=10, pady=10)
button9 = customtkinter.CTkButton(button_frame, button_size, button_size, text="9", font=button_font, command=lambda: num_key(9))
button9.grid(row=0, column=2, padx=10, pady=10)
button_plus = customtkinter.CTkButton(button_frame, button_size, button_size, text="+", font=button_font, command=lambda: operation_key("+"))
button_plus.grid(row=0, column=3, padx=10, pady=10)

button4 = customtkinter.CTkButton(button_frame, button_size, button_size, text="4", font=button_font, command=lambda: num_key(4))
button4.grid(row=1, column=0, padx=10, pady=10)
button5 = customtkinter.CTkButton(button_frame, button_size, button_size, text="5", font=button_font, command=lambda: num_key(5))
button5.grid(row=1, column=1, padx=10, pady=10)
button6 = customtkinter.CTkButton(button_frame, button_size, button_size, text="6", font=button_font, command=lambda: num_key(6))
button6.grid(row=1, column=2, padx=10, pady=10)
button_minus = customtkinter.CTkButton(button_frame, button_size, button_size, text="-", font=button_font, command=lambda: operation_key("-"))
button_minus.grid(row=1, column=3, padx=10, pady=10)

button1 = customtkinter.CTkButton(button_frame, button_size, button_size, text="1", font=button_font, command=lambda: num_key(1))
button1.grid(row=2, column=0, padx=10, pady=10)
button2 = customtkinter.CTkButton(button_frame, button_size, button_size, text="2", font=button_font, command=lambda: num_key(2))
button2.grid(row=2, column=1, padx=10, pady=10)
button3 = customtkinter.CTkButton(button_frame, button_size, button_size, text="3", font=button_font, command=lambda: num_key(3))
button3.grid(row=2, column=2, padx=10, pady=10)
button_multiply = customtkinter.CTkButton(button_frame, button_size, button_size, text="x", font=button_font, command=lambda: operation_key("*"))
button_multiply.grid(row=2, column=3, padx=10, pady=10)

button0 = customtkinter.CTkButton(button_frame, button_size, button_size, text="0", font=button_font, command=lambda: num_key(0))
button0.grid(row=3, column=0, padx=10, pady=10)
button_clear = customtkinter.CTkButton(button_frame, button_size, button_size, text="C", font=button_font, command=clear_key)
button_clear.grid(row=3, column=1, padx=10, pady=10)
button_equal = customtkinter.CTkButton(button_frame, button_size, button_size, text="=", font=button_font, command=equal_key)
button_equal.grid(row=3, column=2, padx=10, pady=10)
button_divide = customtkinter.CTkButton(button_frame, button_size, button_size, text="÷", font=button_font, command=lambda: operation_key("/"))
button_divide.grid(row=3, column=3, padx=10, pady=10)


root.mainloop()