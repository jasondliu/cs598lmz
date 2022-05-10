fn = lambda: None
# Test fn.__code__ is writable.
def test_code_write(self):
    self.assertIs(fn.__code__, fn.__code__)
    try:
        fn.__code__ = fn.__code__
    except TypeError:
        raise self.skipTest("Cannot set .__code__")

def test_code_write2(self):
    # Test when fn.__code__ is replaced.
    self.assertIsNot(fn.__code__, fn.__code__)


def test_code_write_doc(self):
    try:
        fn.__code__.co_doc = fn.__code__.co_doc
    except TypeError:
        raise self.skipTest("Cannot set .co_doc")

def test_code_write_doc2(self):
    fn.__code__.co_doc = "Doc string"
    self.assertEqual(fn.__code__.co_doc, "Doc string")

def test_code_write_doc3(self):
    fn.__code__.co_doc =
