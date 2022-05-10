import weakref
# Test weakref.ref(). __call__()

def function_returning_weakref_to_object(*args, **kwargs):
    o = object()
    o_wr = weakref.ref(o)
    return o_wr

def f():
    o1 = object()
    o1_wr = weakref.ref(o1)
    o2 = o1_wr()
    assert o1 == o2
# Test weakref.proxy(). __call__()

def function_returning_weakref_proxy_to_object(*args, **kwargs):
    o = object()
    o_wr = weakref.proxy(o)
    return o_wr

def f():
    o1 = object()
    o1_wr = weakref.proxy(o1)
    o2 = o1_wr()
    assert o1 == o2
# Test weakref.proxy(). __call__()

def function_returning_weakref_proxy_to_callable(*args, **kwargs):
    def f_o():
        pass
