import gc, weakref

class TestWeakRef(unittest.TestCase):

    def test_basic(self):
        obj = C()
        obj.foo = 1
        obj.bar = 2
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar = "hello"
        obj.foo = 1.1
        obj.bar
