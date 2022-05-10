import ctypes
ctypes.cast(0, ctypes.py_object).value

# Display the Python version.
import sys
print(sys.version)

# Python allows you to assign a single value to several variables simultaneously.
# For example −
a = b = c = 1
print("a = {}, b = {}, c = {}".format(a,b,c))

# You can also assign multiple objects to multiple variables. For example −
a, b, c = 1, 2, "john"
print("a = {}, b = {}, c = {}".format(a,b,c))

# Python Strings
# A string is usually a bit of text (sequence of characters). 
# You can use single or double quotes to build a string.
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string
