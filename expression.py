import tkinter as tk
from math import *
from z3 import *
from io import StringIO
import sys


def evaluate(event):
    try:
        res.configure(text="Result : " + str(eval(entry.get())))
    except:
        x, y, z = Ints('x y z')
        exp = entry.get()
        f = eval(exp)
        result = StringIO()
        sys.stdout = result
        solve(f)
        result_string = result.getvalue()
        res.configure(text="Result : " + str(result_string))

w = tk.Tk()
frame = tk.Frame(w)
w.title("Expression Calculator")
tk.Label(w, text="Your Expression:").pack(padx=10, pady=10)
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack(padx=100, pady=10)
res = tk.Label(w)
res.pack(padx=10, pady=10)
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
frame.pack()
button.pack(pady=10)
w.mainloop()
