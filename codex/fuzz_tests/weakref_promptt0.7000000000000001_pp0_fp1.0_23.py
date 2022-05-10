import weakref
# Test weakref.ref()
class C:
    def __init__(self):
        self.x = 42
    def __del__(self):
        print("Deleted!")

o = C()
r = weakref.ref(o)
print(r())
del o
print(r())
