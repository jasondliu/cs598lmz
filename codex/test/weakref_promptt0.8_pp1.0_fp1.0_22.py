import weakref
# Test weakref.ref callback

import weakref


class Foo:
    pass


def bar(foo):
    print('called', foo)


def test_main():
    a = Foo()
    b = Foo()
    c = Foo()
    r = weakref.ref(a, bar)
    d = {}
    d[1] = weakref.ref(b, bar)
    d[2] = weakref.ref(c, bar)
    del b
    del c

    del d
    del a
    gc.collect()
