"""
Imports the modules.
"""
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkfont
import ttkbootstrap
import time
import random

class WordLoader:
    """
    Loads and validates words from wordlist.txt.
    """
    def __init__(self, filepath):
        self._words = self._load_words(filepath)

    def _load_words(self, filepath):
        with open(filepath, "r") as shawn_fan_is_very_cute:
            return [line.strip() for line in shawn_fan_is_very_cute if line.strip()] 

    def get_words(self, count):
        if count > len(self._words):
            raise ValueError(f"Maximum allowed words: {len(self._words)}") # error msg
        return random.sample(self._words, count)

    def word_count(self):
        return len(self._words)

class AlxType:
    """
    Manages the main functions, such as word generation and statistics,
    and also handles the interaction logic between the GUI and data.
    """
    def __init__(self, words_loader, gui):
        self._words_loader = words_loader
        self._start_time = None
        self._started = False
        self._test_words = []
        self.gui = gui

    def on_keypress(self, event):
        if not self._started:
            self._start_time = time.time()
            self._started = True
            self.update_timer()

    def update_timer(self):
        if self._started:
            elapsed = time.time() - self._start_time
            self.gui.timer_label.config(text=f"Time: {elapsed:.1f}s")
            self.gui.root.after(100, self.update_timer)  # refresh every 100ms

    def start_test(self):
        count_str = self.gui.number_entry.get()
        if not count_str.isdigit():
            messagebox.showerror("Error", "Please enter a valid number")
            return

        count = int(count_str)
        max_words = self._words_loader.word_count()

        if count > max_words:
            messagebox.showerror("Error", f"Maximum allowed words: {max_words}")
            return

        self._test_words = self._words_loader.get_words(count)
        self._start_time = None
        self._started = False

        self.gui.number_entry.config(state="disabled")
        self.gui.number_submit.config(state="disabled")
        self.gui.word_display.config(text=" ".join(self._test_words)) # adds the test words
        self.gui.word_entry.config(state="normal")
        self.gui.word_entry.delete(0, tk.END)
        self.gui.word_entry.focus()

    def end_test(self, event=None):
        typed_text = self.gui.word_entry.get()
        elapsed = time.time() - self._start_time
        typed_words = typed_text.strip().split()

        wpm = round(len(typed_words) / elapsed * 60) if elapsed > 0 else 0
        correct = sum(1 for typed, actual in zip(typed_words, self._test_words) if typed == actual)
        accuracy = round((correct / len(self._test_words)) * 100) if self._test_words else 0

        messagebox.showinfo("Results", f"Great Job! Your typing speed is {wpm} WPM, and your accuracy is {accuracy}%")

        self.gui.number_entry.config(state="enabled")
        self.gui.number_submit.config(state="enabled")
        self.gui.word_entry.config(state="disabled")
        self.gui.timer_label.config(text="Time: 0.0s")
        self._started = False

class BaseApp:
    """
    Base GUI window.
    """
    def __init__(self):
        self.root = ttkbootstrap.Window(themename="cyborg") # you can change the themename to whatever you want
        self.root.title("Typing Speed Tester")
        self.root.geometry("1000x750")
        self.root.minsize(1000, 750)

        self.default_font = tkfont.nametofont("TkDefaultFont")
        self.default_font.configure(family="Courier New", size=24) # default font

    def run(self):
        self.root.mainloop()

class GUI(BaseApp):
    """
    Main app that combines the other classes.
    """
    def __init__(self):
        super().__init__()
        self.word_loader = WordLoader("wordlist.txt")
        self.logic = AlxType(self.word_loader, self)
        self.build_gui()

    def validate_entry(self, text):
        return text.isdecimal() # command for number-only input

    def build_gui(self):
        """
        Creates all of the widgets for the GUI.
        """
        self.title = ttkbootstrap.Label(
            self.root,
            text="AlxType",
            font=("Times New Roman", 48),
            bootstyle="primary"
        )
        self.title.pack(pady=25)

        question = ttkbootstrap.Label(
            self.root,
            text="Enter the amount of words below!",
            bootstyle="info"
        )
        question.pack()

        self.number_entry = ttkbootstrap.Entry(
            self.root,
            validate="key",
            validatecommand=(self.root.register(self.validate_entry), "%S"), # number-only input
            width=10,
            bootstyle="success"
        )
        self.number_entry.pack(pady=10)

        self.number_submit = ttkbootstrap.Button(
            self.root,
            text="Generate Words",
            command=self.logic.start_test, # command for starting the test
            bootstyle="success"
        )
        self.number_submit.pack(pady=10)

        self.word_display = ttkbootstrap.Label(
            self.root,
            text="Words will appear here...",
            wraplength=950,
            bootstyle="secondary"
        )
        self.word_display.pack(pady=25)

        self.word_entry = ttkbootstrap.Entry(
            self.root,
            width=50,
            state="disabled",
            bootstyle="danger"
        )
        self.word_entry.pack(pady=10)

        self.word_entry.bind("<Key>", self.logic.on_keypress)
        self.word_entry.bind("<Return>", self.logic.end_test)

        self.input_submit = ttkbootstrap.Button(
            self.root,
            text="Finished",
            command=self.logic.end_test, # command for ending the test
            bootstyle="danger"
        )
        self.input_submit.pack(pady=10)

        self.timer_label = ttkbootstrap.Label(
            self.root,
            text="Time: 0.0s",
            font=("Courier New", 48),
            bootstyle="primary"
        )
        self.timer_label.place(relx=1.0, anchor="ne", x=-50, y=30)

GUI().run()