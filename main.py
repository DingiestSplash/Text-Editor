# Installs
# tkinter
import tkinter as tk
# customtkinter
import customtkinter as ctk
# ttkbooststrap
import ttkbootstrap as tb

# Local
from theme_change import *
from open_file import *
from save_file import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
           
# Window
window = ctk.CTk()

# Text Box
text_edit =  ctk.CTkTextbox(window, height=600, width=1000)

# Frames
frame_left = ctk.CTkFrame(window, height=800, width=200)
frame_bottom_left = ctk.CTkFrame(window, height=100, width= 150)
frame_top = ctk.CTkFrame(window, height=35, width= 1000)
frame_top_left = ctk.CTkFrame(window, height=50, width=150)  
 
# Buttons   
new_button = ctk.CTkButton(
    frame_left, text="New", command=lambda: new_button_fun(window, text_edit))
save_button = ctk.CTkButton(
    frame_left, text="Save", command=lambda: save_file_fun(window, text_edit))
open_button = ctk.CTkButton(
    frame_left, text="Open", command=lambda: open_file_fun(window, text_edit))

switch_var = ctk.StringVar(value="on")
theme_switch = ctk.CTkSwitch(
    frame_top_left, text="Light / Dark",variable=switch_var, onvalue="on", offvalue="off", command=change_theme)

# New Function
def new_button_fun():
    pass
    

# Main App
def main():
    window.title("Text Editor")
    window.rowconfigure(0, minsize=15)
    window.rowconfigure(1, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    text_edit.grid(row=1, column=1)
    
    new_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    theme_switch.grid(row=3, column=0, padx=5, pady=5, sticky="s")

    frame_top.grid(row=0, column=1)
    frame_top_left.grid(row=0, column=0)
    frame_left.grid(row=1, column=0, sticky="ns")

    
    window.bind("<Control-s>", lambda x: save_file_fun(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file_fun(window, text_edit))
    
    window.mainloop()
    

       
main() 