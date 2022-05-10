import weakref
# Test weakref.ref(method)

class A(object):
    def method(self):
        print "A.method"

a = A()
a_method = a.method

ref = weakref.ref(a_method)
print ref()

del a
print ref()

a_method()
