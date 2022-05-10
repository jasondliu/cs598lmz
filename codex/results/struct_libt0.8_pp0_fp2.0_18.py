import _struct
import time
import unittest

from support import types_ready


class StructTest(unittest.TestCase):

    def test_error(self):
        # Verify that creating Struct subclasses with odd names raises
        # TypeError (see issue #10907).
        with self.assertRaises(TypeError):
            type('struct', (), {})
        with self.assertRaises(TypeError):
            type('struct', (_struct.Struct,), {})
        with self.assertRaises(TypeError):
            type('struct', (Bits(0),), {})

    def test_buffer(self):
        # _buffer_info
        s = _struct.Struct("i")
        self.assertEqual(s.size, struct.calcsize("i"))
        self.assertEqual(s.format, "i")
        b = bytes(s.size)
        self.assertEqual(s._buffer_info(b), (b, 0, s.size))
        self.assertEqual(s._buffer_info(memoryview(b)), (memory
