import types
types.MethodType(lambda self: self.x, None, A)

class B:
    def __init__(self):
        self.x = 5

B.x

class C:
    def __init__(self):
        self.x = 5
    def getx(self):
        return self.x

c = C()
c.getx()

class D:
    def __init__(self):
        self.x = 5
    def __getx(self):
        return self.x
    def getx(self):
        return self.__getx()

