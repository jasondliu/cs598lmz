import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class MyClass(object):
    def __init__(self):
        self.callback = FUNTYPE(self.my_callback)

    def my_callback(self, arg):
        print('my_callback called with arg %s' % arg)
        return 0


def main():
    myobj = MyClass()
    myobj.callback(5)

if __name__ == '__main__':
    main()
</code>

