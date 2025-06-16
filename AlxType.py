from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
import time
import random

# global variables
start_time = None

# load words from the 'wordlist.txt' file
with open("wordlist.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]

def validate_entry(text):
    """
    Only allows numbers.
    """
    return text.isdecimal()

def start_test():
    """
    Starts the typing test. It gets the amount of words from the input,
    generates them and prepares for the user to start typing.
    """
    global test_words, start_time

    try:
        count = int(entry.get())
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number of words.")
        entry.config(state="normal") # 
        entry.delete(0, tk.END)
        entry.focus()
        return

    if count > len(words):
        messagebox.showwarning("Error", f"Not enough words in the list. Please enter a number up to {len(words)}.")
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.focus()
        return

    # select random words for the test
    test_words = random.sample(words, count)
    word_display.config(text=" ".join(test_words))

    # reset the input box
    word_input.config(state="normal")
    word_input.delete(0, tk.END)
    word_input.focus()

    # record the start of the test
    start_time = time.time()

def end_test():
    """
    Ends the typing test, calculates WPM, and displays the results.
    """
    if not test_words or start_time is None:
        messagebox.showwarning("Error", "Start the test first.")
        return

    typed_text = word_input.get().strip()
    typed_words = typed_text.split()

    total_typed = len(typed_words)

    elapsed = time.time() - start_time
    # calculate WPM
    wpm = round((total_typed / elapsed) * 60) if elapsed > 0 else 0

    # display the test results
    word_display.config(
        text=f"Test complete!\nWPM: {wpm}"
    )
    # disable the input of words
    word_input.config(state="disabled")

# GUI setup
# create the main window using ttkbootstrap
root = ttkbootstrap.Window(themename="superhero")
root.title("AlxType - Typing Speed Test")
root.geometry("1600x900")

# title Label
title = ttkbootstrap.Label(
    text="AlxType",
)
title.pack(pady=10)

# instructions Label
instructions = ttkbootstrap.Label(
    text="Enter the number of words for the test:",
)
instructions.pack(pady=10)

# entry widget for the user to input only numbers
entry = ttkbootstrap.Entry(
    validate="key",
    validatecommand=(root.register(validate_entry), "%S"), # makes sure only decimal numbers are entered
    width=10
)
entry.pack(pady=10)

# button to start the test
word_gen = ttkbootstrap.Button(
    text="Generate Words",
    command=start_test,
)
word_gen.pack(pady=10)

# label to display the words for typing
word_display = ttkbootstrap.Label(
    text="Words will appear here...",
    wraplength=1400, # wraps text
)
word_display.pack(pady=25, padx=50)

# entry widget for the user to type the words
word_input = ttkbootstrap.Entry(
    width=50,
    state="disabled" # unable to type until test starts
)
word_input.pack(pady=10)

# button to end the test
submit_input = ttkbootstrap.Button(
    text="Get WPM",
    command=end_test,
)
submit_input.pack(pady=10)

# loops the program
root.mainloop()