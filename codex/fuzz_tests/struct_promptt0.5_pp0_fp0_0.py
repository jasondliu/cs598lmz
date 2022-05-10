import _struct
# Test _struct.Struct

# Use standard format strings
for fmt in ['i', 'h', 'l', 'q', 'f', 'd']:
    st = _struct.Struct(fmt)
    print(st.size)

# Non-standard format string
try:
    st = _struct.Struct('z')
except ValueError:
    pass
else:
    print('Failed to raise ValueError')

# Invalid format string
try:
    st = _struct.Struct('Z')
except ValueError:
    pass
else:
    print('Failed to raise ValueError')

# Invalid format string
try:
    st = _struct.Struct('Z'*100)
except ValueError:
    pass
else:
    print('Failed to raise ValueError')

# Test format string with a count
st = _struct.Struct('3i')
print(st.size)

# Invalid format string
try:
    st = _struct.Struct('3z')
except ValueError:
    pass
else:
    print('Failed to raise ValueError')

# Test format
