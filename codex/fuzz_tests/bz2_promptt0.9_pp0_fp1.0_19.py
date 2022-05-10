import bz2
# Test BZ2Decompressor.eof()
d = bz2.BZ2Decompressor()
buf = d.decompress(bz2.compress(b"this is a test", 1))
# Shouldn't raise EOFError
print(buf.decode())

print("=====================================================")
# BZ2File
import bz2

f = bz2.BZ2File(__file__ + ".bz2")

print(f.read().decode())
