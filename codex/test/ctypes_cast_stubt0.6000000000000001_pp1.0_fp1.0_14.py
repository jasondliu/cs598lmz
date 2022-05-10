import ctypes
ctypes.cast(id(42), ctypes.py_object).value

print(ctypes.cast(id(42), ctypes.py_object).value)


# ## Weak References

# In[ ]:

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print(d['primary'])         # fetch the object if it is still alive
del a                       # remove the one reference
gc.collect()                # run garbage collection right away
