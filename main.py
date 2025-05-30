import tkinter as tk
import ttkbootstrap

root = ttkbootstrap.Window(themename="superhero")
root.title("AlxType")
root.geometry("1600x900")

title = ttkbootstrap.Label(
    text="AlxWeather",
    font=("consolas", 50, "bold"),
    bootstyle = "primary",
)
title.pack(pady=5)

word_input = ttkbootstrap.Entry(
    font=("consolas, 25")
)
word_input.pack(pady=10)

root.mainloop()