# Installs
# tkinter
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
# customtkinter
import customtkinter as ctk


# Save Function
def save_file_fun(window, text_edit):
    filepath= asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")     
 
