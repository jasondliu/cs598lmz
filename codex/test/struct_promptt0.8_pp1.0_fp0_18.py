import _struct
# Test _struct.Struct

# Specification doesn't raise TypeError
for fmt in [
    '@', '@!', '=', '=!',
    's', 's!', 'p', 'p!',
    'b', 'b!', 'h', 'h!',
    'i', 'i!', 'l', 'l!',
    'q', 'q!', 'n', 'n!',
    'P', 'P!', 'I', 'I!',
    'L', 'L!', 'Q', 'Q!',
    'B', 'B!', 'H', 'H!',
    'f', 'f!', 'd', 'd!']:
    _struct.Struct(fmt)

# Invalid formats
for fmt in ['', '@!a', '!', '!@', '@!.', '@!\x00', '@!\xff']:
    raises(struct.error, _struct.Struct, fmt)

# Unsupported formats
