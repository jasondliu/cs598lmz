import bz2
# Test BZ2Decompressor.__init__()

import bz2


class BZ2Decompressor_init(unittest.TestCase):
  
  def test_filter_ok(self):
    self._test_filter_ok(u'abc')
    self._test_filter_ok(unichr(0x2070))

  def test_filter_null(self):
    self._test_filter_reject(unichr(0x0000))
    self._test_filter_reject(unichr(0x005c))
    self._test_filter_reject(unichr(0x005c)+unichr(0x000a))
    self._test_filter_reject(unichr(0x005c)+unichr(0x005c))

  def _test_filter_ok(self, data):
    self._test_decompressor_init(data)
    self._test_decompressor_construct(data)

  def _test_filter_reject(self, data):
    self.assertRaises(ValueError,
                      self._
