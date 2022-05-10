import weakref
# Test weakref.ref(self)
class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.ref = weakref.ref(self)
    def __str__(self):
        return self.val
    def __repr__(self):
        return self.val
a = Node('a')
b = Node('b')
a.next = b
b.prev = a
b.next = Node('c')
print a.next
print a.next.prev
print a.next.prev.ref()

# Test circular reference
class Node(object):
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child = None
    def __str__(self):
        return self.val
    def __repr__(self):
        return self.val
a = Node('a')
b = Node('b')
a.child = b
b.parent = a
b.child = Node('c')
print a
