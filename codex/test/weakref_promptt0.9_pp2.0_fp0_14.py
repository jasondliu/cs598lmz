import weakref
# Test weakref.ref(self) and weakref.ref(self)() in an object with a __del__
# method: call self.__del__ in both cases.

class c:
    def __init__(self, arg):
        self.arg = arg
        self.data = [1, 2, 3]
