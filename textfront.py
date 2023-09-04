import tkinter as tk
from tkinter import ttk
import json
from tkinter import colorchooser
from PIL import ImageColor

selected_color = None
def choose_color():
    global selected_color
    color = colorchooser.askcolor(title="Renk Seçin")[1]
    selected_color = color
    color_code = selected_color
    selected_color = ImageColor.getcolor(color_code, "RGBA")
def update_label_value(value):
    label_opaklik.config(text=value)
def save_config():
    global selected_color, config
    if selected_color is not None:
        config = {
            "main_image_path" : "image.jpg",
            "text": entry_text.get(),
            "output_path": "sonuc.jpg",
            "position": [int(entry_position_x.get()), int(entry_position_y.get())],
            "font_size": int(entry_font_size.get()),
            "color": [(selected_color[0]), (selected_color[1]), (selected_color[2]), (int(opacity_stick.get()))]
        }
    with open("config.json", "w") as config_file:

        json.dump(config, config_file, indent=4)
        mark.destroy()

mark = tk.Tk()
mark.title("WATERMARKER")

#*********************************************************************************************

label_text = ttk.Label(mark, text="text:")
entry_text = ttk.Entry(mark)

label_position = ttk.Label(mark, text="position (X, Y):")
entry_position_x = ttk.Entry(mark)
entry_position_y = ttk.Entry(mark)

label_font_size = ttk.Label(mark, text="text size:")
entry_font_size = ttk.Entry(mark)

label_opaklik_sec = ttk.Label(mark, text="opacity:")

opacity_stick = tk.Scale(mark, from_=0, to=255, orient="horizontal", command=update_label_value)
label_opaklik = ttk.Label(mark, text="")

label_color = ttk.Label(mark, text="text color:")
button_choose_color = ttk.Button(mark, text="choose color", command=choose_color)


button_save = ttk.Button(mark, text="save", command=save_config)

#************************************************************************************************

label_text.grid(row=1, column=0, padx=10, pady=5)
entry_text.grid(row=1, column=1, padx=10, pady=5)

label_position.grid(row=3, column=0, padx=10, pady=5)
entry_position_x.grid(row=3, column=1, padx=10, pady=5)
entry_position_y.grid(row=3, column=2, padx=10, pady=5)

label_font_size.grid(row=4, column=0, padx=10, pady=5)
entry_font_size.grid(row=4, column=1, padx=10, pady=5)

label_color.grid(row=5, column=0, padx=10, pady=5)
button_choose_color.grid(row=5, column=1, padx=10, pady=5)

label_opaklik_sec.grid(row=8, column=0, padx=10, pady=5)
opacity_stick.grid(row=8, column=1, padx=15, pady=10)
label_opaklik.grid(row=8, column=2, padx=10, pady=5)

button_save.grid(row=20, columnspan=4, padx=10, pady=15)


mark.mainloop()