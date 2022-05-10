import _struct
# Test _struct.Struct.
from test.support import captured_stdout


class StructTest(unittest.TestCase):

    def test_pack_error(self):
        # Issue #14665: Struct.pack no longer accepts tuple if it contains
        # only one element.
        for pattern in ('ii', 'i'):
            with capture_stdout():
                with self.assertRaises((structerror, TypeError)):
                    Struct(pattern).pack((3,))
        for pattern in 's', 'ps':
            with capture_stdout():
                with self.assertRaises((structerror, TypeError)):
                    Struct(pattern).pack(('',))


if __name__ == '__main__':
    unittest.main()
