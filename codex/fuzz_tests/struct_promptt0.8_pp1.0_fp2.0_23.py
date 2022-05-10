import _struct
# Test _struct.Struct API with the 'z' format character.
Format = _struct.Struct("z")
self = Format.__new__.__defaults__
TestCase = namedtuple('TestCase', 'args')
test_cases = [TestCase(args=None), TestCase(args=True), TestCase(args=(1,))]
for t in test_cases:
    for x in t.args:
        if x is not True and not isinstance(x, (int, str)):
            continue
        with self.subTest(x):
            self.assertRaises(TypeError, Format.__new__, Format)

class StructTest(unittest.TestCase):
    def test_format(self):
        x = list(range(4))
        for fmt in "bBhHiIlLqQfd":
            strt = _struct.Struct(fmt)
            x[0] += 1
            self.assertEqual(strt.size, struct.calcsize(fmt))
            self.assertRaises(struct.error, strt.pack, *tuple(
