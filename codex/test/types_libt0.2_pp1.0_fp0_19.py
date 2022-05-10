import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1465702
class C:
    "Test for classic classes"
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# Test for SF bug #1466042
class C(object):
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")
