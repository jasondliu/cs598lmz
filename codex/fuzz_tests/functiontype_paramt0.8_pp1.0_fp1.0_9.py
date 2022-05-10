from types import FunctionType
list(FunctionType(lambda x: x).__globals__.values())

"""

"""
    
    [f.name for f in type(list).__subclasses__()]
    ['UserList']

"""

"""

for i in range(15):
    time.sleep(1)
    print(i)

"""

"""

import random

for i in range(10):
    print(random.randint(1, 99))

"""


"""
#
#   global variable
#

a = 10

def f():
    global a
    a = 20
    print(a)

f()
print(a)

"""

"""

a = 10

def f():
    print(a)

f()
print(a)

"""


"""

a = 10

def f():
    global a
    a = 20
    print(a)

f()
print(a)

"""



"""

#
#   local variable
#

a = 10

def f():

