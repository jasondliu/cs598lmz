import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

class X(object):
    def __init__(self):
        self._i = S()

def main():
    py_x = X()
    cp_x = ctypes.cast(id(py_x), ctypes.POINTER(S))
    # This is not correct, it accesses x attribute of py_x.__class__
    print(cp_x.contents.x)

if __name__ == "__main__":
    main()
</code>
This program prints out <code>0</code>.
I would like to be able to manipulate <code>py_x._i</code> via <code>cp_x</code>. How to do it?

UPDATED.
To make it compiling and running, I had to make the following changes:

Name <code>S</code> class to <code>SStructure</code> to avoid conflict with <code>S</code> type defined in <code>ctypes</code>
Add <code>from ctypes import *</code> to make <code>S_St
