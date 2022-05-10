import weakref
# Test weakref.ref(C())
class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name
