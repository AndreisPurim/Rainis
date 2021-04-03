import tkinter as tk
from tkinter import *

################################## FILES ##################################
#------------------------------- OPEN FILES ------------------------------#
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"AzpazIA - {filepath}")
#------------------------------- SAVE FILES ------------------------------#
def save_file():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"AzpazIA - {filepath}")
################################## FILES ##################################
#------------------------------- OPEN FILES ------------------------------#
def getTextInput():
    print(txt_edit.get("1.0","end"))
    
def click(key):
    print(key.char)
    print(txt_edit.get("1.0","end"))
    print(key.widget.index("@%s,%s" % (key.x, key.y)))
################################ TK SETUP #################################
window = tk.Tk()
window.title("AzpazIA")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
#-------------------------------- BUTTONS --------------------------------#
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

# my button
btnRead=tk.Button(fr_buttons, text="Read", command=getTextInput)
btnRead.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
#---------------------------------- TEXT ---------------------------------#
txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")
txt_edit.insert(INSERT, "AspazIA V0.1 ")
txt_edit.insert(END, "created by Andreis Purim")
txt_edit.tag_add("here", "1.8", "1.12")
txt_edit.tag_add("start", "1.24", "1.37")
txt_edit.tag_config("here", background="yellow", foreground="blue")
txt_edit.tag_config("start", background="black", foreground="green")
txt_edit.bind("<Key>", click)



#---------------------------------- LOOP ---------------------------------#=
window.mainloop()