# Installs
# tkinter
import tkinter as tk
# customtkinter
import customtkinter as ctk

# Theme
theme_mode = "dark"

# Light / Dark Theme
#Function
def change_theme():
    global theme_mode
    if theme_mode == "dark":
        ctk.set_appearance_mode("light")
        theme_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        theme_mode = "dark"

