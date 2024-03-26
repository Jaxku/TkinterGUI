
from tkinter import*
root = Tk()
root.title('Packing!')
root.minsize(600,400)

Label(root, text="Red", bg="red", fg="white").pack(side=LEFT, fill=Y)
Label(root, text="lime", bg="lime", fg="black").pack(side=BOTTOM, fill=X)
Label(root, text="blue", bg="blue", fg="white").\
    pack(side=RIGHT, fill=BOTH, padx=30, pady=30, expand=YES)

mainloop()


