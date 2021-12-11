# import required libraries.
from tkinter import *               # GUI Library.
import numpy as np                  # library dealing with numbers.
import matplotlib.pyplot as plt     # Library used for plotting.


# Variables Definition:
accuracy = 0.001             # The step between each point while plotting.
BG_color = "gainsboro"      # Background color of the GUI. white, midnight blue, gainsboro, light sea green

# Define all accepted characters for the equation field.
allowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "^", " ", "x", "X", "."]


# Plotting function
def command_plotButton():
    '''
    This function make sure that all input field are available with acceptable values,
    then it computes the equation and plot it.
    '''
    try:
        if not Entry_Function.get():
            Label_Error.config(text="Equation can't be Empty")
        elif not Entry_Min.get():
            Label_Error.config(text="Min Value can't be Empty")
        elif not Entry_Max.get():
            Label_Error.config(text="Max Value can't be Empty")
        else:
            try:
                minVal = int(Entry_Min.get())   # Convert Min and Max Values from string to integer.
                maxVal = int(Entry_Max.get())
            except:
                Label_Error.config(text="Min and Max Values should be numbers only")
                raise

            symEq = Entry_Function.get()         # Get Input Function.
            plt.title("f(x) = " + symEq)         # Title of the plot
            symEq = symEq.replace("^", "**")     # Convert any ^ to **, to handle power in python.
            symEq = symEq.replace("X", "x")      # Convert and X to x, to handle Case sensitivity in the equation.

            if minVal == maxVal:                 # Check that Minimum and Maximum Values aren't equal.
                Label_Error.config(text="Minimum Value and Maximum Value can't be equal")
            else:
                x = np.arange(minVal, maxVal, accuracy)                 # Get the range of 'x' starting from minimum value to the maximum value with a step of 'accuracy'.
                if all(char in allowedCharacters for char in symEq):    # Assert that the equation contain only accepted characters.
                    Label_Error.config(text="")                         # Clear the Error label from previous errors.
                    y = eval(symEq)                                     # Evaluate the equation 'Y' for all values of x.
                    plt.plot(x, y)                                      # Plot and show the graph with defined axis.
                    plt.xlabel("X values")
                    plt.ylabel("f(x)")
                    plt.show()
                else:
                    Label_Error.config(text="Equation contain only numbers, + - * / ^ and symbol must be X")
    except:
        Label_Error.config(text="Check the input values")


# Create a tkinter object, Assign dimensions and title.
root = Tk()
root.title("Function Plotting Tool")
root.geometry("450x130")

InputFrame = Frame(root, width=450, height=130, background=BG_color)    # Create and place a frame to place widgets in it.
InputFrame.place(x=0, y=0)

# Create and place Label and input for Equation
Label_Function = Label(InputFrame, text="Enter your function: ", fg="black", background=BG_color)
Label_Function.place(x=5, y=15)
Entry_Function = Entry(InputFrame, background=BG_color)
Entry_Function.place(x=140, y=15)

# Create and place Label and input for Minimum Value
Label_Min = Label(InputFrame, text="Minimum Value: ", fg="black", background=BG_color)
Label_Min.place(x=5, y=45)
Entry_Min = Entry(InputFrame, background=BG_color)
Entry_Min.place(x=140, y=45)

# Create and place Label and input for Maximum value
Label_Max = Label(InputFrame, text="Maximum Value: ", fg="black", background=BG_color)
Label_Max.place(x=5, y=75)
Entry_Max = Entry(InputFrame, background=BG_color)
Entry_Max.place(x=140, y=75)

# Create and place Plot Button
Button_Plot = Button(InputFrame, text="Plot", fg="black", command=command_plotButton, bg=BG_color, width=7, height=2)
Button_Plot.place(x=350, y=35)

# Create and place Label for Error Messages
Label_Error = Label(InputFrame, text="", fg="black", background=BG_color)
Label_Error.place(x=50, y=105)

root.mainloop()
