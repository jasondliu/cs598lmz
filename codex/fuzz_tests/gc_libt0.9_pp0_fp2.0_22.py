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
    if ob3 is None:
        print "deallocated"
    else:
        # not deallocated, py.test would give F in this case...
        assert ob3.func is func
        assert ob3.kw is kw
        assert id(ob3) == oid


class Callable:
    def __call__(self):
        pass

class AppTestWeakref:

    def setup_class(cls):
        if option.runappdirect:
            py.test.skip("pure python test")


