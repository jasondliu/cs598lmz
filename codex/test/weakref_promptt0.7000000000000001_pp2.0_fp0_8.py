import weakref
# Test weakref.ref() for bound methods.
# We can't use weakref.proxy() here because it doesn't handle classes which
# override __eq__.

class Myclass1:
    def __init__(self):
        self.data = 0
        self.method = self.__method
        self.ref = weakref.ref(self.method, self.__callback)

    def __method(self, arg):
        self.data = arg

    def __callback(self, arg):
        self.data = arg
        self.method = None


mc1 = Myclass1()

def test():
    mc1.method(1)
    mc1.ref()
    mc1 = None


test()
print(mc1.data)

# --------------------------------------------------------------------

class Myclass2:
    def __init__(self):
        self.data = 0
        self.method = self.__method
        self.ref = weakref.ref(self.method, self.__callback)

    def __method(self, arg):
        self.data = arg

