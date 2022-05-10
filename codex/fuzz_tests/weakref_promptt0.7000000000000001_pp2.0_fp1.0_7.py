import weakref
# Test weakref.ref() with a lambda for the callback.

import types, weakref

def test():

    L = []

    obj = object()

    def f(x):
        L.append(x)

    r = weakref.ref(obj, f)
    assert L == [obj]

    del r
    assert L == [obj, None]

    # Make sure the lambda is removed automatically.
    assert len(weakref.getweakrefs(obj)) == 0


def test_lambda_ref():
    import weakref
    L = []
    obj = object()
    r = weakref.ref(obj, lambda x: L.append(x))
    assert L == [obj]
    del r
    assert L == [obj, None]
    assert len(weakref.getweakrefs(obj)) == 0

if __name__ == "__main__":
    test()
    test_lambda_ref()
