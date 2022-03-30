# import the modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import time
import webbrowser as wb


class LineNumbers(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)

        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self.on_key_press)

        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_press(self, event=None):
        final_index = str(self.text_widget.index(tk.END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))

        self.configure(state='normal', width=width)
        self.delete(1.0, tk.END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')



# Define Main Loop
root = Tk()
root.title("Lipbir - Text Editor")
root.iconbitmap("icon.ico")
root.geometry("1200x660")
# root.resizable(False, False)


# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

#

is_dark = False

def change_theme (e):
    global is_dark
    if is_dark == False:
        my_text.config(insertbackground= "white", background= "#282923", foreground= "#a9b7c6")
    else:
        my_text.config(insertbackground= "black", background= "white", foreground= "black")
    
    is_dark = not is_dark
        
        

bg_color = "white"
cursor_color = "black"
fg_color = "black"


# Create Main Frame
# my_frame = Frame(root)
# my_frame.pack(pady=5)

# Create Scrollbar
text_scroll = Scrollbar(root)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Text Box

my_text = Text(root, width=97, height=25, insertbackground= cursor_color, font=("Consolas", 16), selectbackground="Yellow", selectforeground="black", foreground = fg_color, background = bg_color, undo=True, yscrollcommand=text_scroll.set)
l = LineNumbers(root, my_text, width=1)
l.pack(side=tk.LEFT)
my_text.pack(expand=1)


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
        messagebox.showinfo('information', '     Saved     ')
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
    sure = messagebox.askquestion('Confirmation', 'Do you want to save Changes?')
    if sure == "no":
        root.quit()
    elif sure == "yes":
        save_as_file(e)
    
def view_help ():
    wb.open("https://github.com/shayan-azizi/Notepad/blob/main/README.md")

def send_feedback_help ():
    wb.open("https://github.com/shayan-azizi/Notepad/issues")   
    
def about_us_help ():
    wb.open("https://github.com/shayan-azizi/Notepad")
    
def font_format ():
    pass
 
# File Menu

file_menu = Menu(my_menu ,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="New File", command=lambda: new_file(False), accelerator= "Ctrl + N")
file_menu.add_command(label="Open File", command=lambda: open_file(False), accelerator= "Ctrl + O")
file_menu.add_separator()
file_menu.add_command(label="Save", command=lambda: save_file(False), accelerator= "Ctrl + S")
file_menu.add_command(label="Save As", command=lambda: save_as_file(False), accelerator= "Ctrl + Shift + Y")
file_menu.add_separator()
file_menu.add_command(label = "Change The Theme", command = lambda: change_theme(False))
file_menu.add_separator()
file_menu.add_command(label="Quit", command=lambda: quit_file(False), accelerator= "Ctrl + Q")

# Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command= my_text.edit_undo, accelerator= "Ctrl + Z")
edit_menu.add_command(label="Redo", command= my_text.edit_redo, accelerator= "Ctrl + Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator= "Ctrl + X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator= "Ctrl + C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator= "Ctrl + V")

# Format Menu
format_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Font...", command=font_format)

# Help Menu
help_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="View Help", command=view_help)
help_menu.add_command(label="Send Feedback", command=send_feedback_help)
help_menu.add_separator()
help_menu.add_command(label="About us", command=about_us_help)

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
