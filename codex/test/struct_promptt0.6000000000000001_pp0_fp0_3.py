import _struct
# Test _struct.Struct.__reduce__().

import pickle
import test.test_support

test.test_support.run_unittest(__name__)

class StructTestCase(unittest.TestCase):

    def test_reduce(self):
        s = _struct.Struct(">i")
        self.assertEqual(s.__reduce__(),
                         (s.__class__, (">i",)))
        self.assertEqual(s.__reduce__()[0](*s.__reduce__()[1]), s)
        s = _struct.Struct("<i")
        self.assertEqual(s.__reduce__(),
                         (s.__class__, ("<i",)))
        self.assertEqual(s.__reduce__()[0](*s.__reduce__()[1]), s)
        s = _struct.Struct("=i")
        self.assertEqual(s.__reduce__(),
                         (s.__class__, ("=i",)))
