import gc, weakref
class Node:
    pass
n1 = Node()
n2 = Node()
n1.next = n2
n2.prev = n1
n1.ref = weakref.ref(n1)
n2.ref = weakref.ref(n1)
del n1
del n2
gc.collect()
