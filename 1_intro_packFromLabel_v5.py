
from tkinter import*
root = Tk()

root.minsize(600, 400)

# root.title(welcome)
root.title("Welcome to computer science!")
welcome = Label(root, bg="pink", fg="white",
                text="Welcome", font=("Times", 50, "bold"))\
    .(side=LEFT, fill=Y)


to = Label(root, bg="yellow", fg="purple", text="to",
           font=("Helvetica", 50, "bold")).(side=BOTTOM, fill=X)


ComputerScience = Label(root, bg="black", fg="red", text="Computer Science!",
                            font=("American Horror Story", 50, "bold")).(side=RIGHT, fill=BOTH, padx=30, pady=30, expand=YES)


mainloop()


# window .geometry - to set size of 500px wide x 200px tall
root.geometry("800x400")
root.maxsize(800,400)


root.mainloop()




mainloop()


