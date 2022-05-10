fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
del gi, fn

import _testbuffer

class AbstractWritableBufferTests(unittest.TestCase):

    def test_release_owned(self):
        # This is the same as test_release_not_owned, except that
        # we pass the "owned=True" argument to the buffer constructor.
        # This tests that the buffer correctly releases the object
        # when it's responsible for it, but not when it's not.
        #
        # See issue #8361.
        class MyBytes(bytearray):
            pass
        b = MyBytes(b"abc")
        self.assertEqual(b.__array_interface__['data'][0],
                         id(b))
        buf = memoryview(b, owned=True)
        self.assertEqual(b.__array_interface__['data'][0],
                         id(b))
        del buf
        self.assertEqual(
