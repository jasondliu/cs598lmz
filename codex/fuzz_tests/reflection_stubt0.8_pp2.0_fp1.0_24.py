fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def f():
    return 'f'

def g():
    return 'g'

class C:
    __call__ = f

    def h():
        return 'h'
    h = staticmethod(h)

    def i(self):
        return 'i'
    i = classmethod(i)

    def __eq__(self, other):
        return 'eq(%s, %s)' % (self, other)

    def __lt__(self, other):
        return 'lt(%s, %s)' % (self, other)

    def __add__(self, other):
        return 'add(%s, %s)' % (self, other)

def h():
    return 'h'

o = C()

assert o() == 'f'
assert o.h() == 'h'
assert o.i() == 'i'
assert o == 3 == 'eq(3, 3)'
assert o < 3 == 'lt(3, 3)'
assert o + 3 == 'add(3, 3)'
