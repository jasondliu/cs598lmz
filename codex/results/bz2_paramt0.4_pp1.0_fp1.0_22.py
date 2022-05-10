from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world"))

# bz2.decompress(bz2.compress(b"hello world"))
# TypeError: a bytes-like object is required, not 'str'

# bz2.decompress(bz2.compress("hello world"))
# TypeError: a bytes-like object is required, not 'str'

# bz2.decompress(bz2.compress(b"hello world".decode()))
# TypeError: a bytes-like object is required, not 'str'

# bz2.decompress(bz2.compress("hello world".encode()))
# TypeError: a bytes-like object is required, not 'str'

bz2.decompress(bz2.compress(b"hello world".decode().encode()))

# bz2.decompress(bz2.compress("hello world".decode().encode()))
# TypeError: a bytes-like object is required, not 'str'

