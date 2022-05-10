import weakref
# Test weakref.ref() with a class that has a custom __hash__ method.
# This test is more thorough than test_weakref.py::test_hash_inheritance,
# because it tests the interaction of the custom __hash__ method with
# weakref.ref().
import unittest
import weakref
HASH = 'spam'


class Hashing(object):

    def __hash__(self):
        return HASH


class Test(unittest.TestCase):

    def test_hash_inheritance(self):
        o = Hashing()
        r = weakref.ref(o)
        self.assertEqual(r(), o)
        self.assertEqual(r().__hash__(), HASH)
        self.assertEqual(hash(r()), HASH)
        self.assertEqual(hash(r), HASH)


if __name__ == '__main__':
    unittest.main()
