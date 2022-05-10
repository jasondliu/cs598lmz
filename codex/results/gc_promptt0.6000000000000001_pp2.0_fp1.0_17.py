import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class C(object):
    pass

# This is a circular list
c0 = C()
c0.next = c1 = C()
c1.next = c0

# This is a doubly linked circular list
c0.prev = c1
c1.prev = c0

# This is a doubly linked list
c0.prev = c1
c1.next = c2 = C()
c2.prev = c1

# This is a doubly linked list
c0.prev = c1
c1.next = c2
c2.prev = c1

# This is a singly linked list
c0.next = c1
c1.next = c2
c2.next = c3 = C()

# This is a singly linked list
c0.next = c1
c1.next = c2
c2.next = c3

# This is not a linked list, but we can't get rid of c0
c0.prev = c4 = C()
c4.next = c0

