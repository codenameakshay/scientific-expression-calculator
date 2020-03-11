import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text="Result : " + str(eval(entry.get())))


w = tk.Tk()
frame = tk.Frame(w)
w.title("Expression Calculator")
tk.Label(w, text="Your Expression:").pack(padx = 10, pady = 10)
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack(padx = 100, pady = 10)
res = tk.Label(w)
res.pack(padx = 10, pady = 10)
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
frame.pack()
button.pack(pady = 10)
w.mainloop()
