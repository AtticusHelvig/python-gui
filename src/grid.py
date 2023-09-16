from tkinter import *

root = Tk()

label0 = Label(root, text="Grid System")
label1 = Label(root, text="Is Cool")

label0.grid(row=0, column=0)
label1.grid(row=1, column=0)

root.mainloop()