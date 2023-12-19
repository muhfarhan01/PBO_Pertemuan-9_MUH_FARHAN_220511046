import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()

        if unit_from == "Celcius":
            if unit_to == "Reamur":
                result = 4/5 * temperature
            elif unit_to == "Fahrenheit":
                result = (9/5 * temperature) + 32
            elif unit_to == "Kelvin":
                result = temperature + 273.15

        elif unit_from == "Reamur":
            if unit_to == "Celcius":
                result = 5/4 * temperature
            elif unit_to == "Fahrenheit":
                result = (9/4 * temperature) + 32
            elif unit_to == "Kelvin":
                result = (5/4 * temperature) + 273.15

        elif unit_from == "Fahrenheit":
            if unit_to == "Celcius":
                result = (5/9 * (temperature - 32))
            elif unit_to == "Reamur":
                result = (4/9 * (temperature - 32))
            elif unit_to == "Kelvin":
                result = (5/9 * (temperature - 32)) + 273.15

        elif unit_from == "Kelvin":
            if unit_to == "Celcius":
                result = temperature - 273.15
            elif unit_to == "Reamur":
                result = 4/5 * (temperature - 273.15)
            elif unit_to == "Fahrenheit":
                result = (9/5 * (temperature - 273.15)) + 32

        label_result.config(text=f"Hasil: {result:.2f} {unit_to}")
    except ValueError:
        label_result.config(text="Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konversi Suhu")

label = tk.Label(root, text="Masukkan suhu:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label_from = tk.Label(root, text="Dari:")
label_from.pack()

combo_from = ttk.Combobox(root, values=["Celcius", "Reamur", "Fahrenheit", "Kelvin"])
combo_from.pack()

label_to = tk.Label(root, text="Ke:")
label_to.pack()

combo_to = ttk.Combobox(root, values=["Celcius", "Reamur", "Fahrenheit", "Kelvin"])
combo_to.pack()

convert_button = tk.Button(root, text="Konversi", command=convert_temperature)
convert_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
