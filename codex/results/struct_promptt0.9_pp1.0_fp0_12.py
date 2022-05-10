import _struct
# Test _struct.Struct("<Pi").unpack()

class Test_struct(unittest.TestCase):
    def test_unpack_unsupported(self):
        # Issue #29087 (https://bugs.python.org/issue29087)
        # Certain struct.unpack calls with invalid arguments may segfault
        # when configured with --disable-framework

        # This may raise a BufferError exception in a way that causes
        # test_memoryleak to segfault when run with debug build.
        # In addition, this segfaults with gcc 4.2.1 with llvm-gcc 4.2 on Mac
        # OS X with python compiled in 32-bit mode
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", "", RuntimeWarning)
            try:
                _struct.Struct("<Pi").unpack(b"")
            except (BufferError, struct.error) as e:
                pass
            else:
                self.fail("an empty string unpacked incorrectly")


def test_main():
    support.gen_test_func(Test
