import _struct
# Test _struct.Struct
_struct.Struct("@2H")

# Test in / out atomicobject
import _atomicobject
_atomicobject.atomicobject.test(10)

# Test in / out memoryview
import _testbuffer
try:
    _testbuffer.test_memoryview2()
except AttributeError:
    # Cannot count on the exact implementation, until PEP 3118.
    # Once memoryview.format is standard, this can be removed.
    assert _testbuffer.test_memoryview()

# Test in / out typeobject
import _typeobject
_typeobject.test()

# Test in / out string
import _string
_string.test()

# Test in / out bytearray
import _testbuffer
_testbuffer.test_bytearray()

# Test in / out bytearray iterator
import _testbuffer
_testbuffer.test_bytearray_iter()

# Test in / out float
import _testbuffer
_testbuffer.test_float()

# Test in / out all builtin types
import _testcapi
_testcap
