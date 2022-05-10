import weakref
# Test weakref.ref

print("Test weakref.ref")

class MyClass:
    pass

def callback(ref):
    print("callback")

def test(value):
    ref = weakref.ref(value, callback)
    print("ref:", ref)
    print("ref():", ref())
    print("callback:", callback)
    print("ref.__call__:", ref.__call__)
    print("ref.__call__()", ref.__call__())
    print("ref.callback", ref.callback)
    print("ref.callback():", ref.callback())
    print("callback():", callback())

    print("del value")
    del value
    print("ref()", ref())
    print("ref.__call__()", ref.__call__())
    print("ref.callback()", ref.callback())
    print("callback()", callback())

t = MyClass()
test(t)

t = "abc"
test(t)
