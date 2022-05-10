import ctypes
ctypes.cast(id(self), ctypes.py_object).value

# This is the same as:

self.__dict__

# In fact, the following are all the same:

self.__dict__
type(self).__dict__
type(self).__dict__.__getattribute__(self, '__dict__')
self.__class__.__dict__
self.__class__.__dict__.__getattribute__(self, '__dict__')

# All of these return the same thing: a reference to the __dict__ attribute
# of the type of self.
</code>

