import gc, weakref

def try_weakref(spec):
    func, kw = spec.get('func'), spec.get('kw')
    ob = Callable()
    ob.func = func
    ob.kw = kw
    oid = id(ob)
    wr = weakref.ref(ob)
    ob2 = wr()
    assert ob is ob2, [ob, ob2]
    assert ob2.func is func
    assert ob2.kw is kw
    del ob
    gc.collect()
    ob3 = wr()
