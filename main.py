# import the modules
from tkinter import *
from tkinter import filedialog
from tkinter import font

# Define Main Loop
root = Tk()
root.title("Lipbir - Text Editor")

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
def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Text Editor")
    status_bar.config(text="New File      ")
    
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files",  "*.*")))
    name = text_file
    status_bar.config(text=f'{name}     ')
    name = name.replace("F:/", "")
    root.title(f'{name} - Text Editor')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir= "", title= "Save file", filetypes= (("Text Files", "*.txt"), ("Python Files", "*.py"), ("HTML Files", "*.html"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'{name}     ')
        name = name.replace("C:/", "")
        root.title(f'{name} - Text Editor')
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0 , END))
        text_file.close()
    
# File Menu
file_menu = Menu(my_menu ,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

# Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")


# Create Statusbar At The Bottom Of App
status_bar = Label(root, text= "Ready   ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()