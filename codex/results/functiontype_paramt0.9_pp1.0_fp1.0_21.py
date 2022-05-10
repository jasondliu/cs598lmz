from types import FunctionType
list(FunctionType(function).__globals__)

#Output
['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__file__', '__cached__', 'sys', 'shutil', 'os', 'urllib']
#Note!
list(function.__globals__)
##Output ##
['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__file__', '__cached__', 'sys', 'shutil', 'os', 'urllib']

### Now lets look at a function in a script without importing the script. 

def function():
    import sys
    import shutil
    import os
    import urllib
    import external
    return [sys,shutil,os,urllib]

function()
#Output ##
[<module 'sys' (built-in)>, <module 'shutil' from '/Users/user/anac
