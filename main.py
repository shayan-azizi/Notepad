# import the modules
from tkinter import *
from tkinter import filedialog
from tkinter import font

# Define Main Loop
root = Tk()
root.title("Lipbir - Text Editor")
root.geometry("1200x660")

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="Yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()


# Configure Scrollbar
text_scroll.config(command=my_text.yview())

root.mainloop()