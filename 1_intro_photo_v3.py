
from tkinter import*
root = Tk()
root.title('ANDRE!')

# Creating a reference to the image
cool_image = PhotoImage(file="ANDRE!.gif")

# Placing the image into the label
image_label = Label(root, image=cool_image)
image_label.pack()

# ADding text below the image
text_label = Label(root, text="This is a cool image"
                              " of andre's grandma!",
                   font=("Comic Sans MS", 20, "bold"),
                   fg="green", bg="hot pink")

text_label.pack()

root.mainloop()

