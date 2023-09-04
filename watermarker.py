import tkinter as tk
from tkinter import ttk
import json
import subprocess



def textwatermarkopen():
     subprocess.run(["python", "textwatermark.py"])


def systemwatermarkopen():
     subprocess.run(["python", "systemwatermark.py"])


root= tk.Tk()
root.title("WATERMARKER")

button_mark = ttk.Button(root, text="TEXT WATERMARK", command=textwatermarkopen)
button_system = ttk.Button(root, text="SYSTEM WATERMARK", command=systemwatermarkopen)

button_mark.grid(row=0, columnspan=1, padx=50, pady=50)
button_system.grid(row=1, columnspan=1, padx=50, pady=50)

root.mainloop()