import _struct
# Test _struct.Struct
from test import test_struct
test_struct.test_struct(test_support.get_attribute(test_struct, 'Struct'))

# Test the new buffer interface
from test import test_buffer
test_buffer.test_buffer(test_support.get_attribute(test_buffer, 'ArrayType'))

# Test the new memoryview object
from test import test_memoryview
test_memoryview.test_memoryview(test_support.get_attribute(test_memoryview, 'memoryview'))

# Test the new bytes object
from test import test_bytes
test_bytes.test_bytes(test_support.get_attribute(test_bytes, 'bytes'))

# Test the new bytearray object
from test import test_bytearray
test_bytearray.test_bytearray(test_support.get_attribute(test_bytearray, 'bytearray'))

# Test the new file object
from test import test_file
test_file.test_file(test_support.get_attribute(test_file, 'file'
