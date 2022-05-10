import types
types.IntType

types.LongType

types.FloatType

types.StringType

types.NoneType

# Creating a custom module
# Create a file called mymodule.py with the following contents:

# def say_hi():
#     print('Hi, this is mymodule speaking.')

# __version__ = '0.1'
# Save this file in the same directory where your current script is located.

# Now, to use it, we can import the module named mymodule into our Python program using the import statement.

import mymodule

mymodule.say_hi()

# It is also possible to import only parts from a module, by using the from...import statement.

# For example, from mymodule import say_hi, __version__

# This will import the say_hi() function from the module and make it directly available to us.

# Variables in module are not imported by default.
# You have to specify which variables you want to import from a module.

# You can choose to import all variables from a module by using the asterisk (*) operator.

#
