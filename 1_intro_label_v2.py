
from tkinter import*
root = Tk()


# root.title(welcome)
root.title("Welcome to computer science!")
welcome = Label(root, bg="pink", fg="white",
                text="Welcome", font=("Times", 50, "bold"))


to = Label(root, bg="yellow", fg="purple", text="to",
           font=("Helvetica", 50, "bold"))


ComputerScience = Label(root, bg="black", fg="red", text="Computer Science!",
                            font=("American Horror Story", 50, "bold"))

welcome.pack()
to.pack()
ComputerScience.pack()

# window .geometry - to set size of 500px wide x 200px tall
root.geometry("800x400")
root.maxsize(800,400)


root.mainloop()

