import io
# Test io.RawIOBase.read1() with a C extension class.
# This tests the case where we are not returning the entire string
# with the single call to self->read()
import _testbuffer
import array
io.RawIOBase.read1(_testbuffer.cdata('123', 5))
io.RawIOBase.read1(_testbuffer.cdata('123', 5), 2)
io.RawIOBase.read1(_testbuffer.cdata('123', 5), 1)
io.RawIOBase.read1(_testbuffer.cdata('123', 5), 0)
with self.assertRaises(TypeError):
    io.RawIOBase.read1(_testbuffer.cdata('123', 5), -1)
with self.assertRaises(TypeError):
    io.RawIOBase.read1(_testbuffer.cdata('123', 5), sys.maxsize)
# This tests the case where the entire read fits into the string provided
io.RawIOBase().read1(_testbuffer.cdata('123', 2))
io.RawIOBase().read1(_testbuffer.cdata('123', 3
