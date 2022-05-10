import weakref
# Test weakref.ref with a callable and a keyword argument.
# Bug 736708 pointed out that this didn't work.
import gc


class C(object):
    pass


def f():
    pass


def main():
    obj = C()
    r = weakref.ref(obj, f, hello=1)
    del obj
    gc.collect()
    r()


main()
