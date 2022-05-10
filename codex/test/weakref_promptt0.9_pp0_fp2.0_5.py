import weakref
# Test weakref.ref -- basically a non-callable proxy that
# retains its object alive until there are no more refs to it.

# Test cyclic garbage: make a bunch of linked objects and
# verify that they get freed.

class Node(object):
    pass

def test_ref():
    L = []
    for i in range(10):
        n = Node()
        n.next = n


def test_cyclic_garbage():
    pass


def test_weakref_with_callback():
    # Bug #836021
    # weakref callbacks could die even if they referenced another object
    alive = []
    def callback(*args):
        alive.append(1)
    class A(object):
        pass
    a = A()
    r = weakref.ref(a, callback)
    del a
    gc.collect()
    assert alive == [1]

