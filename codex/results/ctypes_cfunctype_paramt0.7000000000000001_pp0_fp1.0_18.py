import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class baseClass:
    def __init__(self):
        self.base = self
    def aMethod(self, a):
        return "baseClass aMethod called with "+str(a)

class derivedClass(baseClass):
    def __init__(self):
        baseClass.__init__(self)
    def aMethod(self, a):
        return "derivedClass aMethod called with "+str(a)

def callback(a):
    print "callback called with "+str(a)
    return a*2

def main():
    myCallback = FUNTYPE(callback)
    myCallback(5)

    d = derivedClass()
    print d.aMethod(5)
    print d.base.aMethod(5)

if __name__ == '__main__':
    main()
