import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1424246
class C:
    "Test for classic classes"
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

class D(object):
    "Test for new-style classes"
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

for C in C, D:
    a = C()
    a.x = 1
    if a.x != 1: raise TestFailed, 'property failed'
    del a.x
    try:
        print a.x
    except AttributeError:
        pass
    else:
