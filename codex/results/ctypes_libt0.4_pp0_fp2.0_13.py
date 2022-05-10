import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Tiny Calculator")

# Define a function for the button
def click():
    try:
        global expression
        expression = expression + str(value.get())
        equation.set(expression)
    except:
        equation.set("Error")
        expression = ""

# Function to clear the contents
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" Error ")
