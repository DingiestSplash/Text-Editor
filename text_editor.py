# Installs
# tkinter
import tkinter as tk
from tkinter import font as tkFont
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
text_edit =  ctk.CTkTextbox(window, height=600, width=1000, undo=True, font=('Helvetica', 20,))

# Buttons
class Buttons():
# Top   
    new_button = ctk.CTkButton(
        frame_top, text="New", command=lambda: new_button_fun(window, text_edit))

    save_button = ctk.CTkButton(
        frame_top, text="Save", command=lambda: save_file_fun(window, text_edit))

    open_button = ctk.CTkButton(
        frame_top, text="Open", command=lambda: open_file_fun(window, text_edit))

    exit_button = ctk.CTkButton(
        frame_top, text="Exit", command=lambda: exit_button_fun(window, text_edit))

    # Left
    bold_button = ctk.CTkButton(
        frame_left, text="Bold", command=lambda: bold_button_fun(window, text_edit))

    italic_button = ctk.CTkButton(
        frame_left, text="Italic", command=lambda: italic_button_fun(window, text_edit))

    undo_button = ctk.CTkButton(
        frame_left, text="Undo", command=lambda: undo_button_fun(window, text_edit))

    redo_button = ctk.CTkButton(
        frame_left, text="Redo", command=lambda: redo_button_fun(window, text_edit))

# Functions
# Select <--- Cant get to work
def select(window, text_edit):
    selected = text_edit.selection_get()

# Bold Button  
def bold_button_fun(window, text_edit):
    
    selected = text_edit.selection_get()
    
    current_font = text_edit.cget("font")
    current_weight = tkFont.Font(font=current_font).actual()["weight"]

    if current_weight == "normal":
        bold_font = ('TkDefaultFont', 20, 'bold')
        text_edit.configure(font=bold_font)
        if selected:
            text_edit.configure(font=bold_font)            
    else:
        normal_font = ('TkDefaultFont', 20) 
        text_edit.configure(font=normal_font)


# Italic Button        
def italic_button_fun(window, text_edit):
    current_font = text_edit.cget("font")
    current_slant = tkFont.Font(font=current_font).actual()["slant"]

    if current_slant != "italic":
        italic_font = ('TkDefaultFont', 20, 'italic')
        text_edit.configure(font=italic_font)
    else:
        normal_font = ('TkDefaultFont', 20)
        text_edit.configure(font=normal_font)

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
def new_button_fun(window, text_edit):
    text_edit.delete("1.0", "end")

# Exit Button
def exit_button_fun(window, text_edit):
    window.quit()

# Undo Button    
def undo_button_fun(window, text_edit):
    try:
        text_edit.edit_undo()
    except:
        pass  # Nothing to undo

# Redo Button       
def redo_button_fun(window, text_edit):
    try:
        text_edit.edit_redo()
    except:
        pass  # Nothing to redo
