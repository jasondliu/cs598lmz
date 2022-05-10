import _struct
# Test _struct.Struct.__repr__

import test.support

class S(test.support.TestCase):
    def test_repr(self):
        s = _struct.Struct('i')
        self.assertEqual(repr(s), "<_struct.Struct object at 0x%x>" % id(s))

def test_main():
    test.support.run_unittest(S)

if __name__ == "__main__":
    test_main()
