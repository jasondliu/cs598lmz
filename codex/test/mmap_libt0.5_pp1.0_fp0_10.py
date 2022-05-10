import mmap

class MyClass(object):
    def __init__(self):
        self.mf = mmap.mmap(-1, 1024*1024*1024)
        self.mf.seek(0)
    def __del__(self):
        self.mf.close()

def myfunc():
    myobj = MyClass()
    myobj.mf.write('hello')
