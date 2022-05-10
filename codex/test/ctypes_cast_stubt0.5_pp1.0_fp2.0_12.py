import ctypes
ctypes.cast(1, ctypes.py_object)

import sys
sys.getrefcount(1)

#%%
l1 = [1, 2, 3]
l2 = [1, 2, 3]

l1 is l2

#%%
t1 = (1, 2, 3)
t2 = (1, 2, 3)

t1 is t2

#%%
t1 = (1, 2, 3)
t2 = tuple([1, 2, 3])

t1 is t2

#%%
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person('bob')
p2 = Person('bob')

p1 is p2

#%%
p1 == p2

#%%
p1 = Person('bob')
p2 = p1

p1 is p2

#%%
p1 == p2

#%%
p1 = Person('bob')
p2 = p1

p2.name = 'mel'

p1.name
