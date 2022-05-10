import _struct
# Test _struct.Struct.

# Create a type for our test.
st = _struct.Struct("bBhHiIlLqQfd")

# Create an instance of that type.
values = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0)

# Try packing it.
packed = st.pack(*values)

# Try unpacking it.
unpacked = st.unpack(packed)

# See if the packed and unpacked values match.
for i in range(len(values)):
    print("Original:", values[i], "Unpacked:", unpacked[i])
    if values[i] != unpacked[i]:
        print("Mismatch")
