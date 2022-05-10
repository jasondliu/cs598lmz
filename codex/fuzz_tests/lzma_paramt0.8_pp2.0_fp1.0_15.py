from lzma import LZMADecompressor
LZMADecompressor().decompress(data[3:])

# $ ls -lh compressed
# -rwxr-xr-x  1 mzerr  staff   80B Aug 18 16:34 compressed

# $ python decompress.py compressed
# b'Hello from Python!'

# $ echo 'Hello from Python!' > compressed

# $ ls -lh compressed
# -rwxr-xr-x  1 mzerr  staff   17B Aug 18 16:35 compressed

# $ python compress.py compressed
# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

# $ ls -lh compressed
# -rwxr-xr-x  1 mzerr  staff   24B Aug 18 16:35 compressed

# $ xxd -p compressed
# fd377a585a00004e6d6b4459012101160074002
