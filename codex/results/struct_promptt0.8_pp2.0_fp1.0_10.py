import _struct
# Test _struct.Struct.__ne__(other)


class TestNE(unittest.TestCase):

    def test_equal_same_object(self):
        s = _struct.Struct('i')
        self.assertTrue(not s != s)

    def test_equal_two_instances(self):
        s1 = _struct.Struct('i')
        s2 = _struct.Struct('i')
        self.assertTrue(not s1 != s2)

    def test_differ_format(self):
        s1 = _struct.Struct('i')
        s2 = _struct.Struct('I')
        self.assertTrue(s1 != s2)


def test_main():
    with test_support.check_py3k_warnings(
        ("struct.__ne__\(\) not supported in 3.x",
         DeprecationWarning)):
        test_support.run_unittest(TestNE)


if __name__ == "__main__":
    test_main()
