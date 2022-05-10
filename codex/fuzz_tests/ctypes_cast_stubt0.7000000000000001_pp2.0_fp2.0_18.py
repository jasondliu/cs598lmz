import ctypes
ctypes.cast(1, ctypes.py_object)

s = '3.14159'
I = int(s)
F = float(s)
print I, F

# The built-in function eval takes a string and returns a value
x = 1
print eval('x+1')
print eval('+1')
print eval('*'*10)

# The built-in function exec takes strings and either executes them as Python programs or
# evaluates them in the scope where it was called
exec 'x=x+1'
print x

# The built-in function dir is used to find out which names a module defines
import sys, math
print dir(sys)
print dir(math)

# The built-in function help provides online documentation for modules, classes and functions
print help(sys.exit)

# The standard functions map and filter
# map: return a list
print map(ord, 'spam')
print map((lambda x: x**2), range(5))

# filter: return a list
print filter((lambda x: x%2 == 0), range(5))

#
