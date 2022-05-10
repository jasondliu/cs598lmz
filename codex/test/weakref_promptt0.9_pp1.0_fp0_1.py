import weakref
# Test weakref.ref.
d = weakref.ref(object())

class C:
    pass

# Test weakref.proxy.
def _test_weakref_proxy(Proxy, o):
    try:
        p = Proxy(o)
    except TypeError:
        print('Could not create a proxy for a %s' % type(o))
    else:
        print('%s(%s())' % (Proxy.__name__, type(o).__name__))
        p.some_attr = 3
        print('%r, %r' % (p.some_attr, o.some_attr))

_test_weakref_proxy(weakref.proxy, C())

# Test weakref.WeakValueDictionary.
def _test_weak_value_dict(Dict, o):
    d = Dict({id(o): o})
    print(type(d), d[id(o)])
    del o # depend on gc
    for i in range(2):
        print('Step', i)
        gc.collect()
