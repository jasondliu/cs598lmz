import weakref
# Test weakref.ref(self) and weakref.ref(self)() in an object with a __del__
# method: call self.__del__ in both cases.

class c:
    def __init__(self, arg):
        self.arg = arg
        self.data = [1, 2, 3]
        print "__init__ %s %s" % (self, self.data)

    def __del__(self):
        print "__del__ %s %s" % (self, self.data)
        if hasattr(self, 'data'):
            self.data.remove(3)

c_o = c(3)
r_o = weakref.ref(c_o)

print "ref is %s" % (r_o)
print "ref() is %s" % (r_o())
print "ref() is %s" % (r_o())

del r_o

print "del() ref()"

del c_o

print "del() object"

def test_basics():
    # Create a cycle, then
