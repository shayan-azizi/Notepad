# import the modules
from tkinter import *
from tkinter import filedialog
from tkinter import font
import time
import keyboard

# Define Main Loop
root = Tk()
root.title("Lipbir - Text Editor")
root.iconbitmap("icon.ico")

# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Comic Sans MS", 16), selectbackground="Yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()


# Configure Scrollbar
text_scroll.config(command=my_text.yview())

# Create Menubar
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Menu Tools
def new_file(e):
    my_text.delete("1.0", END)
    root.title("New File - Text Editor")
    status_bar.config(text="New File      ")
    global open_status_name
    open_status_name = False
    
    
def open_file(e):
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files",  "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=f'{name}     ')
    name = name.replace("F:/", "")
    root.title(f'{name} - Text Editor')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def save_as_file(e):
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir= "", title= "Save file", filetypes= (("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved:  {name}     ')
        name = name.replace("C:/", "")
        root.title(f'{name} - Text Editor')
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0 , END))
        text_file.close()

def save_file(e):
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0 , END))
        text_file.close()
        status_bar.config(text=f'Saved:  {open_status_name}     ')
    else:
        save_as_file(e)
        
def cut_text (e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text (e):
    global selected
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text (e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

def quit_file (e):
    root.quit()
    
 
# File Menu
file_menu = Menu(my_menu ,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="New File                Ctrl + N", command=new_file)
file_menu.add_command(label="Open File               Ctrl + O", command=open_file)
file_menu.add_command(label="Save                       Ctrl + S", command=save_file)
file_menu.add_command(label="Save As     Ctrl + Shift + S", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Quit                       Ctrl + Q", command=quit_file)

# Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo                       Ctrl + Z")
edit_menu.add_command(label="Redo                        Ctrl + Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut                           Ctrl + X", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy                         Ctrl + C", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste                        Ctrl + V", command=lambda: paste_text(False))


# Create Statusbar At The Bottom Of App
status_bar = Label(root, text= "Ready   ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Bindings
root.bind("<Control-x>", cut_text)
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-S>", save_as_file)
root.bind("<Control-q>", quit_file)

root.mainloop()