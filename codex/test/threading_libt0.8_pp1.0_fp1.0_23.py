import threading
threading.ThreadError
# example of importing a module
import math
print(math.sqrt(25))
# example of importing a module
import math as mt
print(mt.sqrt(25))
# example of importing a module
from math import sqrt
print(sqrt(25))
# example of importing a module
from math import *
print(sqrt(25))
# example of importing a module
from math import sqrt as square
print(square(25))
# import the copy module
import copy
# copy an int
x = 1
y = copy.copy(x)
print(x)
print(y)
# copy a string
x = "Guru99"
y = copy.copy(x)
print(x)
print(y)
# copy a list
x = [1, 2, 3]
y = copy.copy(x)
print(x)
print(y)
# copy a tuple
x = (1, 2, 3)
y = copy.copy(x)
print(x)
print(y)
# copy a dictionary
