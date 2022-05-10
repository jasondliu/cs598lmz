import weakref
# Test weakref.ref(self)
class A:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "A(" + self.name + ")"

a = A("a")
wref = weakref.ref(a)
print(wref)
del a
print(wref)
print(wref())

# Test weakref.finalize(self, fn, *args, **kwargs)
def callback(wref):
    print("Finalized", wref())

a = A("a")
wref = weakref.finalize(a, callback, wref)
wref()
print("Deleting", a)
del a
print("Deleted")
print(wref())

# Test weakref.WeakValueDictionary().data
a = A("a")
d = {id(a): a}
wvd = weakref.WeakValueDictionary.fromkeys(d.keys())
for k in d:
    wvd[k] = d[k]
print(wvd)
del d
