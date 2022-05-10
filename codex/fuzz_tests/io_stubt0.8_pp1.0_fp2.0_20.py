import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
print(view)
del view

class MyDeallocator(ctypes.c_void_p):
    def __init__(self, func, *args):
        self.func = func
        self.args = args
    def __del__(self):
        self.func(*self.args)

def g():
    ctypes.pythonapi.Py_DecRef(MyDeallocator(print, "ok"))

g()
del g
