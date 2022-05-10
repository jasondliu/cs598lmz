import weakref
# Test weakref.ref(obj, callback)


class MyClass:
    pass


def callback(obj):
    print("callback called with", obj)


obj = MyClass()
ref = weakref.ref(obj, callback)
print("obj:", obj)
print("ref:", ref)
print("ref():", ref())
print("obj:", obj)
print("deleting obj")
del obj
print("obj:", obj)
print("ref():", ref())
print("callback:", callback)
print("ref:", ref)
print("ref():", ref())


def callback(obj):
    print("callback called with", obj)


obj = MyClass()
ref = weakref.ref(obj, callback)
print("obj:", obj)
print("ref:", ref)
print("ref():", ref())
print("obj:", obj)
print("deleting obj")
del obj
print("obj:", obj)
print("ref():", ref())
print("callback:", callback)
print("ref:", ref)
print("ref():", ref())
print("
