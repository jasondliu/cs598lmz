from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.format = '&lt;h' 
s.size = calcsize(s.format)

# Pack a string into a binary buffer.
with open('ascii_text.txt', "r") as input_file:
    input_text = input_file.read()

binary_data = bytearray(s.size + len(input_text))
binary_buffer = memoryview(binary_data)

offset = 0

# Pack the data
offset += s.pack_into(binary_buffer, offset, len(input_text))
offset += binary_buffer[offset:offset+len(input_text)].cast("B").cast("b").cast("B").tobytes()

# Unpack the data
offset = 0

n_chars = s.unpack_from(binary_buffer, offset)[0]
offset += s.size

text = binary_buffer[offset:offset+n_chars].cast("B").tobytes()
</code>

