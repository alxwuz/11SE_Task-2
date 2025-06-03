"""
Import modules
"""
import tkinter as tk
import ttkbootstrap

"""
Display the 'WPM' when run
"""
def get_wpm():
    wpm = ttkbootstrap.Label(
        text="great typing, your wpm is 9999!!", # It's too early to implement a working feature, so this is what will do for now.
    )
    wpm.pack(pady=5)

"""
Create the GUI for the test
"""
root = ttkbootstrap.Window(themename="superhero") # A theme for all of the text, buttons, etc. (using ttkbootstrap)
root.title("AlxType")
root.geometry("1600x900") # How big the window will start when launched (yes, it's resizable)

"""
Create the title
"""
title = ttkbootstrap.Label(
    text="AlxType",
)
title.pack(pady=5)

"""
The prompt for the user to type
"""
prompt = ttkbootstrap.Label(
    text="Type: shawn fan is a very cute boy who is good at maths",
)
prompt.pack(pady=5)

"""
An input box so the user can type the words
"""
word_input = ttkbootstrap.ScrolledText(
    width=25,
    height=5,
)
word_input.pack(pady=10)

"""
A submit button that gets the WPM when pressed
"""
submit_input = ttkbootstrap.Button(
    text="Submit",  
    command=get_wpm, # This is the command that displays the word count
    bootstyle="outline button"
)
submit_input.pack()

"""
Start the GUI until closed
"""
root.mainloop()