import tkinter as tk
from tkinter import ttk
import winsound

def on_click(event):
    text = event.widget.cget("text")
    play_button_sound(text)
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def play_button_sound(text):
    sounds = {
        "+": "sound_add.wav",
        "-": "sound_subtract.wav",
        "*": "sound_multiply.wav",
        "/": "sound_divide.wav",
        "sin": "sound_sin.wav",
        "cos": "sound_cos.wav",
        "tan": "sound_tan.wav",
        "log": "sound_log.wav",
        "sqrt": "sound_sqrt.wav",
        "pow": "sound_pow.wav",
        "=": "sound_equal.wav",
        "C": "sound_clear.wav",
        "(": "sound_open_bracket.wav",
        ")": "sound_close_bracket.wav",
        "0": "sound_0.wav",
        "1": "sound_1.wav",
        "2": "sound_2.wav",
        "3": "sound_3.wav",
        "4": "sound_4.wav",
        "5": "sound_5.wav",
        "6": "sound_6.wav",
        "7": "sound_7.wav",
        "8": "sound_8.wav",
        "9": "sound_9.wav",
        ".": "sound_decimal.wav",
    }
    sound_file = sounds.get(text, "sound_click.wav")
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Styles for ttk (themed Tkinter) widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 20), padding=10)

entry = tk.Entry(root, font=("Arial", 20), bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Calculator buttons
buttons = [
    ("7", "8", "9", "/", "sin", "cos"),
    ("4", "5", "6", "*", "tan", "log"),
    ("1", "2", "3", "-", "sqrt", "pow"),
    ("0", ".", "C", "+", "(", ")")
]

for i in range(4):
    for j in range(6):
        btn = ttk.Button(root, text=buttons[i][j])
        btn.grid(row=i+1, column=j, sticky=tk.NSEW)
        btn.bind("<Button-1>", on_click)

# Special "=" button
equal_btn = ttk.Button(root, text="=")
equal_btn.grid(row=5, column=4, columnspan=2, sticky=tk.NSEW)
equal_btn.bind("<Button-1>", on_click)

# Configure grid weights to resize buttons with window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

root.mainloop()
