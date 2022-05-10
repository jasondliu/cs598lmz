import weakref
# Test weakref.ref and weakref.proxy objects

from test import support

# Base class for testing weakref.ref and weakref.proxy
class RefTest:
    # Subclasses should override the following attributes:
    thetype = None
    can_compare = True

    def setUp(self):
        self.o = C()
        self.r = self.thetype(self.o)

    def tearDown(self):
        self.o = None
        self.r = None

    def test_basic(self):
        self.assertEqual(self.r(), self.o)
        self.assertEqual(self.r.__class__, self.thetype)
        self.assertEqual(self.r.__hash__(), hash(self.o))
        self.assertEqual(self.r.__bool__(), bool(self.o))

    def test_call(self):
        self.assertEqual(self.r(), self.o)

    def test_str(self):
        self.assertEqual(str(self.r), str(self.o))
