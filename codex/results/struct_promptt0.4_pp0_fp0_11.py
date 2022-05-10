import _struct
# Test _struct.Struct

# Create a Struct object
st = _struct.Struct('I 2s f')

# Create a bytes object
values = (1, b'ab', 2.7)
print('Original values:', values)

# Pack the bytes
packed_data = st.pack(*values)
print('Format string  :', st.format)
print('Uses           :', st.size, 'bytes')
print('Packed Value   :', packed_data)

# Unpack the bytes
unpacked_data = st.unpack(packed_data)
print('Unpacked Value :', unpacked_data)
