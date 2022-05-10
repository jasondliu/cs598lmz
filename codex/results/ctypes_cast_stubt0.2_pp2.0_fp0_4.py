import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getrefcount(x)

#%%
y = x
sys.getrefcount(x)

#%%
del x
sys.getrefcount(y)

#%%
del y

#%%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

#%%
p = Point(2, 3)
str(p)

#%%
repr(p)

#%%
print(p)

#%%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({
