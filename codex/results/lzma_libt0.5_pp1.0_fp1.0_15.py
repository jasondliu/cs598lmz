import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x1f\xf3')

# The result is the same as the previous example.

# Compression

# The LZMA library supports five compression modes:

# fast (mode 0)
# normal (mode 1)
# extra (mode 2)
# maximum (mode 3)
# ultra (mode 4)
# The default mode is normal. The following example shows how to compress a string using the default mode:

import lzma
lzma.compress(b'Hello world!')

# The result is a bytestring that starts with the header bytes 0xFD, 0x37, 0x7A, 0x58, 0x5A, 0x00, 0x00, 0x04, 0xE6, 0xD6, 0xB4, 0x46, 0x02, 0x00, 0x21, 0
