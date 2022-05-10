import io
# Test io.RawIOBase compatibility
io.BytesIO().readinto1(array.array('B'))

try:
    import _io
# Test _io.IOBase compatibility
_io.BytesIO().readinto1(array.array('B'))
except ImportError:
    pass
</code>
Where this is the code I'm using in the test.
<code>    def test_array_buffer(self):
        self.buffer = io.BytesIO(self.data)
        self.buffer.readinto1(self.array)
        self.assertEqual(self.array, self.array_result)
</code>

