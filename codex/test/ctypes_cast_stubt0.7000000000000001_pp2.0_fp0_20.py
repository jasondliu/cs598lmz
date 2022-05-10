import ctypes
ctypes.cast(0x100, ctypes.c_void_p).value

# Question 4
# What does the following code print?

class A(object):
    def __init__(self):
        self.a = 1
