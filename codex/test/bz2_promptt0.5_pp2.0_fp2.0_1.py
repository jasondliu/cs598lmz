import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is the original data")

decompressor = bz2.BZ2Decompressor()

print("Input is %d bytes" % len(data))
print("Output is %d bytes" % len(decompressor.decompress(data)))
print("Remaining %d bytes in %r" % (len(decompressor.unused_data), decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()

for chunk in [data[:4], data[4:8], data[8:12], data[12:]]:
    print("Input is %d bytes" % len(chunk))
    try:
        print("Output is %d bytes" % len(decompressor.decompress(chunk)))
    except IOError as e:
        print("Error:", e)
    print("Remaining %d bytes in %r" % (len(decompressor.unused_data), decompressor.unused_data))

# Test BZ2Compressor

