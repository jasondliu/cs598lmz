import weakref
# Test weakref.ref(C())
class C:
    def __init__(self):
        self.c = 1
    def __del__(self):
        print("C.__del__")

d = weakref.ref(C())
print(d(), d().c)
d().c = 2
print(d(), d().c)
del d().c
print(d(), d().c)
