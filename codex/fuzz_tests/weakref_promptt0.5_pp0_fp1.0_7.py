import weakref
# Test weakref.ref() and weakref.proxy() on a class instance

class C:
    pass

class D:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print("r():", r())
print("p.__class__:", p.__class__)
print("p.__class__.__name__:", p.__class__.__name__)
print("p.__dict__:", p.__dict__)
#print(p.__dict__ is o.__dict__)
print("p.__doc__:", p.__doc__)
print("p.__hash__():", p.__hash__())
print("p.__init__:", p.__init__)
print("p.__module__:", p.__module__)
print("p.__new__:", p.__new__)
print("p.__reduce__:", p.__reduce__)
print("p.__reduce_ex__:", p.__reduce_ex__)

