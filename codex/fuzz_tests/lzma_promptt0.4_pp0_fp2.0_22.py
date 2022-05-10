import lzma
# Test LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

decomp = lzma.LZMADecompressor()

try:
    decomp.decompress(data)
except EOFError:
    print("EOFError")

try:
    decomp.decompress(b"")
except EOFError:
    print("EOFError")

try:
    decomp.decompress(b"\x00\x00")
except EOFError:
    print("EOFError")

try:
    decomp.decompress(b"\x00\x00\x00\x00")
except EOFError:
    print("EOFError")

try:
    decomp.decompress(b"\x00\x00\x00\x00\x00")
except EOFError:

