import ctypes
# Test ctypes.CFUNCTYPE in a class
class Test(object):
    def __init__(self):
        self.foo = ctypes.CFUNCTYPE(None)
        if self.foo is None:
            raise Exception("self.foo is None")

Test()
</code>
This is the compile command I use:
<code>C:\Users\user\dev\python\foo&gt;C:\Users\user\dev\python\pcbuild\python.exe setup.py build --compiler=mingw32
running build
running build_ext
</code>
I'm using MinGW-w64 to compile the C code, Python 2.7.6, and ctypes 0.9.9.8 if that helps.


A:

I think I figured it out. I had to include the Python.h header file in the C code. I also had to define a <code>PyObject*</code> type using the following line:
<code>PyMODINIT_FUNC initfoo(void);
</code>

