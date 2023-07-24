import tkinter as tk
from Calculator_Module import add, subtract, multiply, divide
from Scienctific_Module import square_root, sin, cos, tan
import math

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        evaluate_expression()
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Exit":
        root.quit()
    else:
        entry.insert(tk.END, text)

def scientific_button_click(event):
    text = event.widget.cget("text")
    if text == "π":
        entry.insert(tk.END, math.pi)
    elif text == "e":
        entry.insert(tk.END, math.e)
    elif text == "sqrt":
        expression = entry.get()
        result = math.sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "sin":
        expression = entry.get()
        result = math.sin(math.radians(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "cos":
        expression = entry.get()
        result = math.cos(math.radians(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif text == "tan":
        expression = entry.get()
        result = math.tan(math.radians(eval(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+",
    "=", "Exit"
]

for i in range(5):
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    for j in range(4):
        idx = i * 4 + j
        if idx < len(buttons):
            text = buttons[idx]
            button = tk.Button(frame, text=text, font=("Arial", 20), relief="ridge", bd=3)
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            button.bind("<Button-1>", button_click)

scientific_buttons = [
    "π", "e", "sqrt",
    "sin", "cos", "tan"
]

scientific_frame = tk.Frame(root)
scientific_frame.pack(fill=tk.BOTH, expand=True)

for i in range(2):
    for j in range(3):
        idx = i * 3 + j
        if idx < len(scientific_buttons):
            text = scientific_buttons[idx]
            button = tk.Button(scientific_frame, text=text, font=("Arial", 15), relief="ridge", bd=3)
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            button.bind("<Button-1>", scientific_button_click)

root.mainloop()
