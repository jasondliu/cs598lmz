import weakref
# Test weakref.ref classes.


class MyClass(object):

    def __init__(self):
        self.callback = self.method

    def method(self, arg):
        """Return argument arg+1."""
        return arg + 1

    @property
    def prop(self):
        return 1


class MySubClass(MyClass):

    @property
    def prop(self):
        return super().prop + 1


class TestWeakMethod:

    def callback(self, arg):
        """Return argument arg+1."""
        return arg + 1

    def class_method(cls, arg):
        """Return argument arg+1."""
        return arg + 1

    def test_creation(self):
        """Check weakreference to a method."""
        obj = MyClass()
        x = weakref.ref(obj.callback)
        self.assertEqual(x().__self__, obj)
        self.assertRaises(TypeError, weakref.ref, obj.method)

    def test_call(self):
        obj = MyClass()
        x = weakref
