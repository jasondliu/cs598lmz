import weakref
# Test weakref.ref() and weakref.contains() on methods.


class TestContains2Methods:

    def __init__(self):
        self.data = 1
        self.method = self.__class__.getdata

    def __del__(self):
        pass

    def getdata(self):
        return self.data

    def check(self, mr, wr):
        assert mr() == wr()
        assert mr() == wr.__self__
        return wr

    def run(self):
        o = self
        wm = weakref.ref(o.getdata)
        wm2 = weakref.ref(o.method)
        assert self.check(wm, wm2)
        assert weakref.contains(self.check(wm, wm2), self)
        wr = weakref.ref(self)
        assert weakref.contains(wr, self)


def test_main():
    TestContains2Methods().run

# test_contains2_methods()
