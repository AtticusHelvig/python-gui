from tkinter import *

root = Tk()

def click():
    text = entry.get()
    print(text)

entry = Entry(root, width=50, borderwidth=5)
entry.insert(0, "Enter your name: ")
entry.pack()

button = Button(root, text="Enter", command=click)
button.pack()

root.mainloop()