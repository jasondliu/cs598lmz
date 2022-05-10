fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()"""
        self.assertRaises(TypeError, self.exec_fn, s)

    def test_truncate(self):
        self.assertRaises(ValueError, self.code.co_code.replace, b'\x00', b'')

        self.code.co_code = b'abc'
        self.assertRaises(ValueError, self.code.co_code.replace, b'\x00', b'\x00\x00')

        self.code.co_code = b'\x00'
        self.assertRaises(ValueError, self.code.co_code.replace, b'\x00', b'\x00\x00')

        self.code.co_code = b'\x00'
        self.assertRaises(ValueError, self.code.co_code.replace, b'\x00', b'')

        self.code.co_code = b'ab\x00'
        self.assertRaises(ValueError, self.code.co_code.replace, b'\
