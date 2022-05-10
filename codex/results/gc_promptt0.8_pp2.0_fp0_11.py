import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs to old-style classes
class C(object):
    pass

c = C()
gc.collect()
assert gc.collect() == 0
w = weakref.ref(c)
del c
assert gc.collect() == 0


def callback():
    print('a'*12)


w = weakref.ref(c, callback)
del c
assert gc.collect() == 0
del w
assert gc.collect() == 1
print('ok')


class Test:
    def __init__(self):
        self.track = []

    def __del__(self):
        self.track.append("")

track = []
created = []

def create():
    o = Test()
    o.track = track
    created.append(o)
    return o

def g(n):
    if n:
        g(n-1)
    create()

def main():
    for i in range(20):
        g(i)
    del created
    n = gc.collect()
    assert n
