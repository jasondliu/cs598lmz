import _struct
# Test _struct.Struct

# Create a test structure
test_struct = _struct.Struct('i?f')

# Pack it into a string
packed_data = test_struct.pack(23, 0, 42.0)

# Create an array
import array

# Unpack data into the array
test_array = array.array('c', packed_data)

# Create a mutable memoryview
buffer = memoryview(test_array)

# Init an iterator on the buffer
iterator = iter(buffer)

# Iterate through buffer
while True:
    try:
        elt = next(iterator)
    except StopIteration:
        break
    print(elt)

# Create a bytes array
import array
test_array = array.array('c', b'This is a test')

# Create a memoryview from the array
buffer = memoryview(test_array)

# Slice the memoryview
buffer[4:8]

# Create a memoryview from a bytes object
buffer = memoryview(b'This is a test')

# Slice the memoryview
buffer[4:
