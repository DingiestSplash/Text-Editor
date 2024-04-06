# Installs
# tkinter
import tkinter as tk
from tkinter import filedialog
# customtkinter
import customtkinter as ctk
# ttkbooststrap
import ttkbootstrap as tb

# Local
from theme_change import *
from text_editor import *

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Theme Change
theme_mode = "dark"
switch_var = ctk.StringVar(value="on")
theme_switch = ctk.CTkSwitch(
    frame_top_left, text="Light / Dark",variable=switch_var, onvalue="on", offvalue="off", command=change_theme)
   
            
# Main App
def main():
    
    window.title("Text Editor")
    window.rowconfigure(0, minsize=15)
    window.rowconfigure(1, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    text_edit.grid(row=1, column=1)
    
    # Buttons - Left Nav
    new_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    theme_switch.grid(row=3, column=0, padx=5, pady=5, sticky="s")
    # Buttons - Top Nav
    bold_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    italic_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    undo_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
    redo_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

    frame_top.grid(row=0, column=1)
    frame_top_left.grid(row=0, column=0)
    frame_left.grid(row=1, column=0, sticky="ns")

    
    window.bind("<Control-s>", lambda x: save_file_fun(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file_fun(window, text_edit))
    
    window.mainloop()
    

       
main() 