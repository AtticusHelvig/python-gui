from tkinter import *

root = Tk()

def click():
    label = Label(root, text="You clicked.")
    label.pack()

button1 = Button(root, text="Click Me!", command=click, bg="gray")
button1.pack()

root.mainloop()