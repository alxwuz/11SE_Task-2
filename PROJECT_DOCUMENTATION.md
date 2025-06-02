# 11SE Task 2 2025 - Typing Speed Tester
## By Alex

# Sprint 1
## **Requirements Definition**
### **Functional Requirements**
- **Data Retrieval:** What does the user need to be able to view in the system? 

The user needs to be able to view the words for the typing test which has randomised words, which will end once the user has typed the set amount of words words. The system will then gather the data from the user's test and calculate the WPM (Words Per Minute) from it.

- **User Interface:** What is required for the user to interact with the system?

They need to be able to type the displayed words so that they can test their typing skills. There will also be an option to select the amount of words the user wants to do, and the deafult will be 25. If the user makes an error during the typing test, they will lose accuracy. There will also be an exit button on the UI or on the window.

- **Data Display:** What information does the user need to obtain from the system? What needs to be output for the user?

The user will get their results for the typing test. It will show their WPM from the typing test that they completed, as well as how long it took them to type all of it.

### **Non-functional Requirements**
- **Performance:** How well does the system need to perform? 

The system needs to be able to register the input from the user without a big delay for a quick measurement when calculating the results from the user's test.

- **Reliability:** How reliable does the system and data need to be?

The program needs to be fully reliable, as any innacuracies when gathering the data will result an inaccurate display of the WPM.

- **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

The system navigation needs to be easy to use with minimalistic design featuring the main parts of the test as well as other elements. There will also be a guide on how to use the program within the README.md file.

## **Determining Specifications**
### **Functional Secifications**
- **User Requirements**
    - What does the user need to be able to do? List all specifications here.

The user needs to be able to start the test, write the displayed words, which then they will recieve their feedback. The system should be easy to use and allow the user to reset or exit the test whenever it is needed.

- **Inputs & Outputs**
    - What inputs will the system need to accept and what outputs will it need to display?

In the test, the user will take the keyboard's input from the user as they do the test, and will display statistics while the user is typing, such as time passed during the test or words typed, etc.

- **Core Features**
    - At its core, what specifically does the program need to be able to do?

The essential features that the program needs to are displaying the passage of text, show the statistics while doing the test, and calculate the inputs from the user and clearly display the results on the graphical user interface (GUI).

- **User Interaction**
    - How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?

Users will interact with the program with a GUI with clear navigation, where they are able to complete the test and view their results on how well they did.

- **Error Handling**
    - What possible errors could you face that need to be handled by the system?

Some errors that can happen in the program include empty inputs, not following the specified words for the test, etc. The program must be able to handle these problems without breaking the whole system as it would result in a big inconvenience.

### **Non-functional Specifications**
- **Performance**
    - How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?

The system will need to respond instantly to the user's input. A fast system response keeps the users engaged, so the program needs to be optimized to keep it running without delays or any problems.

- **Useability / Accessibility**
    - How might you make your application more accessible? What could you do with the User Interface to improve usability?

To improve accessibility in the program, there could be support such as readable fonts, larger buttons, as well as adding different languages. The usability can be improved by not making the UI too complex and making it a simple design.

- **Reliability**
    - What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Illogical calculation? Menu navigation going to wrong places?

Some minor errors that could happen in the system include innacurate WPM calculations or not getting the raw input from the user. These problems will need to be tested to ensure the program runs smoothly.

### **Use Cases**
- **Actors:** Who interacts with the system (e.g., user, external system).

Someone who wants to test their typing skills using the application.

- **Preconditions:** Conditions that must be met before the use case starts.

The application needs to be open and running, with the words for the test loaded and ready to be started.

- **Main Flow:** The step-by-step process of how the interaction occurs.

1. The user opens the application
2. They select the configurations for the test.
3. They start typing after the words are loading.
4. The system collects the data from the typing and calculates the analytics.
5. After the user finishes, the data gathered from the test is displayed.

**Postconditions:** The expected outcome or result after the use case is completed.

The user is given results on their test, and is met with two buttons which either restart or exit the test.

## **Design**
![alt text](images/storyboard.png)

### **Data Flow Diagrams**
#### Level 0
![alt text](images/level0.png)

#### Level 1
![alt text](images/level1.png)

### **Gantt Chart**
![alt text](images/gantt.png)

## **Build and Test**
```
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
```

## **Review**
1. **Evaluate**

Right now, the program is just a very simple GUI, acting as a foundation for future improvements. Currently, users are able to submit the words that are typed, adhering to the prompt that is displayed above the text box, which fufils the basic funcitonal and non-functional requirements that was mentioned earlier.

2. **Analyse**

The program is performing well, it just needs to be improved upon during the next sprints. Currently, the program cannot calculate the WPM, so it just displays a text after the user submits the test, following the use-case, and handling the input and output well.

3. **Assess**

As for the code structure, it is well-written and coherent. The comments accurately label what the code is doing, and is structured well with lines seperating different parts of the code. The variables are named accurately, and overall, the code is structured neatly.

4. **Explain**

In the future, the WPM calculation will actually be implemented along with some GUI features, improving the aestethic of the program and improving the user's experience. There can also be some added features to the code structure, such as the comments being more detailed.

## **Launch**

# Sprint 2
## **Design**

## **Build and Test**

## **Review**

## **Launch**

# Sprint 3
## **Design**

## **Build and Test**

## **Review**

## **Launch**

# Sprint 4
## **Design**

## **Build and Test**

## **Review**

## **Launch**