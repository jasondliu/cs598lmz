import gc, weakref


class C(object):
    __slots__ = ('a',)


dct = {0: weakref.WeakKeyDictionary(), 1: deque()}
class D(object):
    __slots__ = ('a',)
    def __del__(self):
        global dct
        t = type(self)
        dct[id(t)][t] = 1


def callback(ignored):
    pass

class E(object):
    def __del__(self):
        global dct
        t = type(self)
        dct[id(t)][t] = 1


class F(E):
    __slots__ = ('a',)


class G(object):
    __slots__ = ('a', '__dict__')


def test_weakref_slot():
    global dct
    # weakref.proxy(instance)
    i = C()

    x = weakref.ref(i, callback)
    p = weakref.proxy(i, callback)

    weakref.ref(p)

   
