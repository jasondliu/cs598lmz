import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() returns bytes, and bz2.decompress() expects bytes.
# So you must convert str to bytes with str.encode() first.

bz2.decompress(bz2.compress(b'hello world'))

bz2.decompress(bz2.compress(b'hello world')).decode()

# bz2.decompress() returns bytes, so you must convert it to str with bytes.decode()

bz2.decompress(bz2.compress(b'hello world')).decode()

bz2.decompress(bz2.compress(b'hello world')).decode() == 'hello world'

# bz2.compresslevel
# The compresslevel argument to bz2.compress() controls the tradeoff between speed and compression.
# Higher values of compresslevel result in better compression, but slower compression and decompression.
# The default value is 9, which is
