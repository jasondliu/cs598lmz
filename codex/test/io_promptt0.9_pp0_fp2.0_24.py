import io
# Test io.RawIOBase.read1() with a C extension class.
# This tests the case where we are not returning the entire string
# with the single call to self->read()
import _testbuffer
import array
