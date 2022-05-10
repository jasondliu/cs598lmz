fn = lambda: None
gi = (i for i in ())
fn.__code__ = (0, 0, 0, 0, 0, 0x4000, 0, 0, 0, 0, 0)


class PyCodeFlag(unittest.TestCase):
    def test_flag(self):
        # Test that __code__.co_flags only contains set flags
        for flag in range(0x8000):
            fn.__code__ = (0, 0, 0, 0, 0, flag, 0, 0, 0, 0, 0)
            self.assertTrue(fn.__code__.co_flags == flag)

    def test_equality(self):
        # Test that Flag values compare correctly
        self.assertEqual(PyCF_MASK, PyCF_MASK)
        self.assertEqual(PyCF_MASK, 0x83F)

    def test_sense(self):
        # Test that Flag values can be used to test flag values
        self.assertTrue(PyCF_MASK & 0x80)
        self.assertTrue(PyCF_MASK & 0x2)
        self.assertFalse(PyCF_MASK & 0x4000
