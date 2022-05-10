import _struct
# Test _struct.Struct.

# Create a Struct object, and use it to pack and unpack data.

import _struct

s = _struct.Struct('hhl')
values = (1, 2, 3)
print(s.pack(*values))
print(s.unpack(s.pack(*values)))

# Create a Struct object with a format that uses the '!' modifier.

s = _struct.Struct('!hhl')
values = (1, 2, 3)
print(s.pack(*values))
print(s.unpack(s.pack(*values)))

# Create a Struct object with a format that uses the '@' modifier.

s = _struct.Struct('@hhl')
values = (1, 2, 3)
print(s.pack(*values))
print(s.unpack(s.pack(*values)))

# Create a Struct object with a format that uses the '=' modifier.

s = _struct.Struct('=hhl')
values = (1, 2, 3)
print(s.pack(*values))
print(s.unpack(s.pack
