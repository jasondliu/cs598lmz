import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1465409
class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")
