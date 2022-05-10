import _struct
import _testcapi
from io import StringIO
from StringIO import StringIO
from _stringio import StringIO
from collections import namedtuple


def _test(test_case, **options):
    test_case(**options)
    gc.collect()


class PickleTests(unittest.TestCase):
    # Most tests are in test_cpickle, this one only contains tests for
    # pickle-specific features.

    def test_pickling_null_bytes(self):
        l = ['a', 'b', 'c']
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            s = pickle.dumps(l, proto)
            self.assertEqual(s.count(b'\x80'), 1,
                             "Failed on proto %d: %r" % (proto, s))
            self.assertIn(b'N', s,
                          "Failed on proto %d: %r" % (proto, s))
            self.assertEqual(pickle.loads(
