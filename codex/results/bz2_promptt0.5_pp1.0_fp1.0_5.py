import bz2
# Test BZ2Decompressor

data = b"".join(line.encode("utf-8") for line in open("/usr/share/dict/words", "rt"))
compressed = bz2.compress(data)
print(compressed)

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

print(decompressed == data)

decompressor = bz2.BZ2Decompressor()
for chunk in compressed:
    print(decompressor.decompress(chunk))

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed[:60])
decompressor.decompress(compressed[60:])

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed[:60])
try:
    decompressor.decompress(compressed[60:])
except IOError as err:
    print(err)

decompressor
