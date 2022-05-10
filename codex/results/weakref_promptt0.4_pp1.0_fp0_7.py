import weakref
# Test weakref.ref to a class instance

class A:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return "A(%s)" % self.val

a = A(10)
r = weakref.ref(a)
print r()
print r() is a

a = A(20)
print r()
print r() is a

del a
print r()

print "-" * 20

# Test weakref.ref to a class instance with a __del__ method

class B:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return "B(%s)" % self.val
    def __del__(self):
        print "B.__del__"

b = B(10)
r = weakref.ref(b)
print r()
print r() is b

b = B(20)
print r()
print r() is b

del b
print r()

print "-" * 20
