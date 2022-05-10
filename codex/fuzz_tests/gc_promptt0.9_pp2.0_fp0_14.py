import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() (which calls tp_clear() and tp_dealloc()).
# Test manual invocation of tp_clear() and tp_dealloc().

# Test clearing of containers

class TestBase(object):
    def __init__(self):
        from sys import getrefcount as grc
        self.setrefcnt = grc(self)
        print 'tb.__init__()', object.__init__(self)
    def __del__(self):
        print 'tb.__del__()'
    def __repr__(self):
        return '<TestBase>'

class Test1(TestBase):
    def __init__(self):
        TestBase.__init__(self)
        self.l = []
    def __del__(self):
        print 't1.__del__()'
        TestBase.__del__(self)

class Test2(TestBase):
    def __init__(self):
        TestBase.__init__(self)
        self.d = {}
    def __del__(
