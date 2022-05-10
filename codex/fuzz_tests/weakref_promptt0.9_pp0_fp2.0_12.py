import weakref
# Test weakref.ref on old-style classes

class C(object):
    pass

class D:
    def __init__(self):
        self.x = 42


for cls in [C, D]:
    obj = cls()
    ref1 = weakref.ref(obj, lambda x: 0/0)
    print("one time:", ref1())
    ref2 = weakref.ref(obj, lambda x: 0/0)
    try:
        obj.x = None
    except AttributeError:
        pass
    print("two times:", ref2())
    try:
        print("as instance:", obj.__weakref__())
        print("repr:", repr(obj.__weakref__()))
        print("str:", str(obj.__weakref__()))
    except AttributeError:
        print("skipped because of AttributeError")
    try:
        print("as class:", cls.__weakref__)
        print("repr:", repr(cls.__weakref__))
        print("str:", str(
