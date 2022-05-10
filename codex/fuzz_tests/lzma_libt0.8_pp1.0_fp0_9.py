import lzma
lzma.LZMAError()

print(lzma.__doc__)
print(lzma.__package__)
print(lzma.__path__)



class Testlzma(unittest.TestCase):
  def setUp(self):
    self.x = lzma.LZMAError()
    self.y = lzma.LZMADecompressor()
    self.z = lzma.LZMACompressor()

  def tearDown(self):
    self.x = None
    self.y = None
    self.z = None

  def testAttributes(self):
    self.assertRaises(AttributeError, getattr, self.x, '__dict__')
    self.assertRaises(AttributeError, getattr, self.x, '__weakref__')
    self.assertRaises(AttributeError, getattr, self.x, '__bases__')
    self.assertRaises(AttributeError, getattr, self.x, '__mro__')

  def testDecompressor(self
