import os
import platform
import psutil
import json
import tkinter as tk
from tkinter import ttk
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

def bytes_to_gb(bytes_value):
    gb_value = bytes_value / (1024 ** 3)
    return round(gb_value)

def convert(data):
    data_gb = {}
    for key, value in data.items():
        if isinstance(value, int):
            data_gb[key] = bytes_to_gb(value)
        elif isinstance(value, dict):
            data_gb[key] = convert(value)
        else:
            data_gb[key] = value
    return data_gb

def save_sconfig():
    global sconfig
    sconfig = {
            "text": all_info,
            "main_image_path": "image.jpg",
            "output_path": "sonuc.jpg",
            "position": [int(entry_position_x.get()), int(entry_position_y.get())],
            "font_size": int(entry_font_size.get()),
            "color": [(selected_color[0]), (selected_color[1]), (selected_color[2]), (int(opaklik_stick.get()))]
    }
    with open("sconfig.json", "w") as json_file:
        json.dump(sconfig, json_file, indent=4)
    info.destroy()

def get_disk_info():
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            'Total': partition_info.total,
            'Used': partition_info.used,
            'Free': partition_info.free,
            'Percent': partition_info.percent
        }
    return disk_info
disk_info = get_disk_info()
disk_info = convert(disk_info)

def get_memory_info():
    memory_info = {}
    virtual_memory = psutil.virtual_memory()
    memory_info['Total'] = virtual_memory.total
    memory_info['Available'] = virtual_memory.available
    memory_info['Used'] = virtual_memory.used
    memory_info['Percent'] = virtual_memory.percent
    return memory_info
memory_info = get_memory_info()
memory_info = convert(memory_info)

def get_basic_info():
    basic_info = {
        'User Name': os.getlogin(),
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor()

    }
    return basic_info
basic_info = get_basic_info()

def get_network_info():
    network_info = {}
    net_io = psutil.net_io_counters()
    network_info['Total Bytes Sent'] = net_io.bytes_sent
    network_info['Total Bytes Received'] = net_io.bytes_recv
    return network_info
network_info = get_network_info()

disk_info_text = "\n".join([f"{key}: {value}" for key, value in disk_info.items()])
memory_info_text = "\n".join([f"{key}: {value}" for key, value in memory_info.items()])
basic_info_text = "\n".join([f"{key}: {value}" for key, value in basic_info.items()])
network_info_text = "\n".join([f"{key}: {value}" for key, value in network_info.items()])

# Tüm bilgileri alt alta yazan bir metin oluştur
all_info = f"System:\n{basic_info_text}\n\nMemory (GB):\n{memory_info_text}\n\nDisk (GB):\n{disk_info_text}\n\nNetwork:\n{network_info_text}"

info = tk.Tk()
info.title("System Info")


label_position = ttk.Label(info, text="position (X, Y):")
entry_position_x = ttk.Entry(info)
entry_position_y = ttk.Entry(info)

label_font_size = ttk.Label(info, text="text size:")
entry_font_size = ttk.Entry(info)

label_opaklik_sec = ttk.Label(info, text="opacity:")

opaklik_stick = tk.Scale(info, from_=0, to=255, orient="horizontal", command=update_label_value)
label_opaklik = ttk.Label(info, text="")

label_color = ttk.Label(info, text="text color:")
button_choose_color = ttk.Button(info, text="choose color", command=choose_color)

button_save = ttk.Button(info, text="save", command=save_sconfig)

label_position.grid(row=3, column=0, padx=10, pady=5)
entry_position_x.grid(row=3, column=1, padx=10, pady=5)
entry_position_y.grid(row=3, column=2, padx=10, pady=5)

label_font_size.grid(row=4, column=0, padx=10, pady=5)
entry_font_size.grid(row=4, column=1, padx=10, pady=5)

label_color.grid(row=5, column=0, padx=10, pady=5)
button_choose_color.grid(row=5, column=1, padx=10, pady=5)

label_opaklik_sec.grid(row=8, column=0, padx=10, pady=5)
opaklik_stick.grid(row=8, column=1, padx=15, pady=10)
label_opaklik.grid(row=8, column=2, padx=10, pady=5)

button_save.grid(row=20, columnspan=4, padx=10, pady=15)

info.mainloop()