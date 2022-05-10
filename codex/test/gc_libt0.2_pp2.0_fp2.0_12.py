import gc, weakref

def test_weakref_callback():
    class Foo(object):
        pass

