
from tkinter import*
root = Tk()

root.title("My first window")

# window .geometry - to set size of 500px wide x 200px tall
root.geometry("500x200")
root.maxsize(800,400)


greeting = Label(text="Hello, Tkinter!")

greeting.pack()

root.mainloop()

