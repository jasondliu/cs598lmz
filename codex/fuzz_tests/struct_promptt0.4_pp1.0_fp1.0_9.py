import _struct
# Test _struct.Struct.format

# Test that the format string is verified.
try:
    _struct.Struct("")
except ValueError:
    pass
else:
    print("expected ValueError")

try:
    _struct.Struct("@")
except ValueError:
    pass
else:
    print("expected ValueError")

try:
    _struct.Struct("@!")
except ValueError:
    pass
else:
    print("expected ValueError")

try:
    _struct.Struct("@ii")
except ValueError:
    pass
else:
    print("expected ValueError")

# Test that the format string is stored.
s = _struct.Struct("@i")
print(s.format, s.size, s.format_size)

s = _struct.Struct("@ii")
print(s.format, s.size, s.format_size)

s = _struct.Struct("@iii")
print(s.format, s.size, s.format_size)

s = _struct.Struct("@iiii")
print(s.
