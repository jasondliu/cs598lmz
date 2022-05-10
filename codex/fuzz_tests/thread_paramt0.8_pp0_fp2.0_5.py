import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello ")).start()
threading.Thread(target=lambda:sys.stdout.write("world")).start()

# Packages
### creating a package
# A directory must contain a file named __init__.py (even empty) to make a directory a Python package
# creating file abs.py in mypkg/
# and a file __init__.py in mypkg/
# to use mypkg/abs.py
import mypkg.abs
mypkg.abs.abs('abc')

# the from keyword can help us not to use the package and module names
from mypkg import abs
abs.abs('abc')

# from and as
from mypkg.abs import abs as abso
abso("12")

# __all__
# __all__ variable in __init__.py: can restrict what names can be imported from a module in the package
# __all__ variable in abs.py

from mypkg.abs import *

#for your information, the abs object is an abs class
print("abs type: ", type(abs))
abs("abc")

