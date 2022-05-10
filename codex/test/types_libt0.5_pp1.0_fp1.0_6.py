import types
types.StringType

# __file__ is a global variable that is set to the filename of the file that is currently being executed
import os
print(os.path.dirname(os.path.abspath(__file__)))

# Execute the file
execfile('/Users/michael/GitHub/Python-Notes/Basics/Hello.py')

# Functions
# def defines a function
