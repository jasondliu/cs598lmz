import weakref
# Test weakref.ref objects.

# XXX This should use a list of weakrefs
# to check that no callbacks are triggered by the GC.

class Dummy:
    def __init__(self, n):
        self.n = n
