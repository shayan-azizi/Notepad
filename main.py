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

# Create Menubar
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Menu Tools
# File Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File")
file_menu.add_command(label="Open File")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Quit")

# Edit Menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")


root.mainloop()