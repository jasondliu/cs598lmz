import weakref
# Test weakref.ref
class Test(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "<Test value=%d>" % (self.value,)
def test_ref():
    import weakref
    def create_test(i):
        return Test(i)
    x = create_test(10)
    r = weakref.ref(x)
