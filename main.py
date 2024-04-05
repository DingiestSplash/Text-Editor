import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# Open Function
def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")    

# Save Function
def save_file(window, text_edit):
    filepath= asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")
# New Function
def new_button():
    text_edit.delete("0.0", "end")

# Light / Dark Theme
theme_mode = "dark"
def change_theme():
    global theme_mode
    if theme_mode == "dark":
        ctk.set_appearance_mode("light")
        theme_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        theme_mode = "dark"              

def main():
    # Variables
    # Window
    window = ctk.CTk()
    # Text Box
    text_edit =  ctk.CTkTextbox(window, height=600, width=1000)
    # Frame
    frame = ctk.CTkFrame(window, height=800)
    # Buttons        
    new_button = ctk.CTkButton(
        frame, text="New", command=lambda: new_button(window, text_edit))
    save_button = ctk.CTkButton(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = ctk.CTkButton(
        frame, text="Open", command=lambda: open_file(window, text_edit))
    switch_var = ctk.StringVar(value="on")
    theme_switch = ctk.CTkSwitch(
        frame, text="Light / Dark",variable=switch_var, onvalue="on", offvalue="off", command=change_theme)
    

    
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    text_edit.grid(row=0, column=1)
    
    new_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    theme_switch.grid(row=3, column=0, padx=5, pady=5, sticky="s")

    frame.grid(row=0, column=0, sticky="ns")
    
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    
    window.mainloop()
    

       
main() 