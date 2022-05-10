import types
types.StringType

# __file__ is a global variable that is set to the filename of the file that is currently being executed
import os
print(os.path.dirname(os.path.abspath(__file__)))

# Execute the file
execfile('/Users/michael/GitHub/Python-Notes/Basics/Hello.py')

# Functions
# def defines a function
def hello():
    print 'hello'

# Functions can take arguments
def hello2(name):
    print 'hello', name

# Functions can return values
def hello3(name):
    return 'hello', name

# Functions can return multiple values
def hello4(name):
    return 'hello', name, 'how are you?'

# Functions can return multiple values as a tuple
def hello5(name):
    return 'hello', name, 'how are you?',

# Functions can take multiple arguments
def hello6(name, name2):
    print 'hello', name, 'and', name2

# Functions can take an arbitrary number of arguments
def hello7(*args):

