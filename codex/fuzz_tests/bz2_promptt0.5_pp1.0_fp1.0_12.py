import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
data += bz2.compress(b"this is a test")

d = bz2.BZ2Decompressor()
print(d.decompress(data))
print(d.decompress(data))

try:
    print(d.decompress(b"garbage"))
except Exception as e:
    print("Error:", e)

d = bz2.BZ2Decompressor()
print(d.decompress(data[:4]))
print(d.decompress(data[4:]))

try:
    print(d.decompress(b"garbage"))
except Exception as e:
    print("Error:", e)

print(d.unused_data)

# Test BZ2Decompressor.__repr__
d = bz2.BZ2Decompressor()
print(repr(d))

d.decompress(b"asdf")
print(repr(d))
