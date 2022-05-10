import weakref
# Test weakref.ref
for name in dir(weakref):
    obj = getattr(weakref, name)
    if (isinstance(obj, type) and
        issubclass(obj, weakref.ref) and
        obj is not weakref.ref):
        print(obj, ":")
        for base in obj.mro()[:-1]:
            print("    ", base.__name__)
        obj()

# Test weakref.finalize
for name in dir(weakref):
    obj = getattr(weakref, name)
    if (isinstance(obj, type) and
        issubclass(obj, weakref.finalize) and
        obj is not weakref.finalize):
        print(obj, ":")
        for base in obj.mro()[:-1]:
            print("    ", base.__name__)
        obj()
