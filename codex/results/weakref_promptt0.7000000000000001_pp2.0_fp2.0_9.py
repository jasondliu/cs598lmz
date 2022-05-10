import weakref
# Test weakref.ref() and weakref.ref(obj)

class A:
    def __init__(self):
        self.b = 42

def test(testcase):
    ra = weakref.ref(testcase)
    if ra() is not testcase:
        raise Exception
    if ra() is None:
        raise Exception
    a = A()
    if a.b != 42:
        raise Exception
    ra = weakref.ref(a)
    if ra().b != 42:
        raise Exception
    a.b = 43
    if ra().b != 43:
        raise Exception
    del a
    if ra() is not None:
        raise Exception
    try:
        ra().b
        raise Exception
    except ReferenceError:
        pass

test(test)
