import _struct
# Test _struct.Struct
from test import test_struct
test_struct.test_main()

# Test _struct.Struct in the face of hard-to-find bugs.
test_struct.test_unpack_from()
test_struct.test_unpack_from_buffer()
test_struct.test_pack_into()
test_struct.test_pack_into_buffer()

# Test _struct.Struct with buffer objects.
test_struct.test_buffer_object()

# Test _struct.Struct with array objects.
test_struct.test_array_object()

# Test _struct.Struct with memoryview objects.
test_struct.test_memoryview_object()

# Test _struct.Struct with bytearray objects.
test_struct.test_bytearray_object()

# Test _struct.Struct with unicode format strings.
test_struct.test_unicode_format()

# Test _struct.Struct with struct.pack_into() and struct.unpack_from().
test_struct.test_pack_into_and_unpack_from()

# Test
