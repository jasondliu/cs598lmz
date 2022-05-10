fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = fn.__code__._replace(co_varnames='')

class Obj:
    pass
# Test __dict__
obj = Obj()
obj.__dict__ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

class TestSlots:
    # Test __slots__
    __slots__ = ('a', 'b', 'c', 'd')
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

slots = TestSlots()

class TestBoth:
    __slots__ = ('c', 'd')
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

both = TestBoth()
