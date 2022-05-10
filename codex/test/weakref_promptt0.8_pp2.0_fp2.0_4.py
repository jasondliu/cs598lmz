import weakref
# Test weakref.ref(child).is_alive()

class Parent(object):
    def __init__(self, child):
        self.child_ref = weakref.ref(child)
        self.child_id = id(child)

    def is_child_alive(self):
        return self.child_ref is not None and self.child_ref() is not None

    def get_child_id(self):
        return self.child_id

class Child(object):
    def __init__(self, i, p):
        self.parent = p
        self.i = i

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Child):
            return False
        return self.parent() is other.parent() and self.i == other.i

    def __repr__(self):
        return "Child({}, parent={})".format(self.i, self.parent())

