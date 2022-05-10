import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

class PyFunction(object):
    def __init__(self, f):
        self.__f = FUNTYPE(f)
    def __call__(self, *args):
        return self.__f(*args)

def pymain():
    print("in pymain")
    f = PyFunction(lambda x,y: x+y)
    print(f(1,2))

def main():
    print("in main")
    pymain()

main()
</code>

