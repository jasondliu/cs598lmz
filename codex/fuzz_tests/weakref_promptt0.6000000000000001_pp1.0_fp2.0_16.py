import weakref
# Test weakref.ref(x) with custom __del__ method

class Foo:
    def __del__(self):
        print("Foo.__del__", end=" ")

class Bar(object):
    def __del__(self):
        print("Bar.__del__", end=" ")

f = Foo()
b = Bar()
r = weakref.ref(f)
r2 = weakref.ref(b)
print("before")
del f, b
print("during")
print(r())
print(r2())
print("after")
