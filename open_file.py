# Installs
# tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename
# customtkinter
import customtkinter as ctk


# Open Function
def open_file_fun(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")