# Installs
# tkinter
import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
# customtkinter
import customtkinter as ctk



# Window
window = ctk.CTk()

# Frames
frame_left = ctk.CTkFrame(window, height=800, width=200)
frame_bottom_left = ctk.CTkFrame(window, height=100, width= 150)
frame_top = ctk.CTkFrame(window, height=35, width= 1000)
frame_top_left = ctk.CTkFrame(window, height=50, width=150) 

# Text Box
text_edit =  ctk.CTkTextbox(window, height=600, width=1000, undo=True)

# Buttons   
new_button = ctk.CTkButton(
    frame_left, text="New", command=lambda: new_button_fun(window, text_edit))

save_button = ctk.CTkButton(
    frame_left, text="Save", command=lambda: save_file_fun(window, text_edit))

open_button = ctk.CTkButton(
    frame_left, text="Open", command=lambda: open_file_fun(window, text_edit))

bold_button = ctk.CTkButton(
    frame_top, text="Bold", command=lambda: bold_button_fun(window, text_edit))

italic_button = ctk.CTkButton(
    frame_top, text="Italic", command=lambda: italic_button_fun(window, text_edit))

undo_button = ctk.CTkButton(
    frame_top, text="Undo", command=lambda: undo_button_fun(window, text_edit))

redo_button = ctk.CTkButton(
    frame_top, text="Redo", command=lambda: redo_button_fun(window, text_edit))


# Functions

# Select <--- Cant get to work
def select():
    selected = text_edit.selection_get()

# Bold Button  
def bold_button_fun():   
    bold_font = font.Font(text_edit, text_edit.cget("font"))
    bold_font.configure(weight="bold")
    
    text_edit.tag_config("bold", font=bold_font)
    
    current_tags = text_edit.tag_names("sel.first")
    
    if "bold" in current_tags:
        text_edit.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_edit.tag_add("bold", "sel.first", "sel.last")

# Italic Button        
def italic_button_fun():   
    pass

# Undo Button        
def undo_button_fun():   
    pass

# Redo Button        
def redo_button_fun():   
    pass

# Open Button
def open_file_fun(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")
    
# Save Button
def save_file_fun(window, text_edit):
    filepath= asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")
    
# New Button
def new_button_fun():
    pass 
