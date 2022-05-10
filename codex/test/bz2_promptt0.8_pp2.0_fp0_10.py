import bz2
# Test BZ2Decompressor

compressed_data = bz2.compress(b"this is a test")

print("Original:", len(b"this is a test"))
print("Compressed:", len(compressed_data))

decompressor = bz2.BZ2Decompressor()

output = decompressor.decompress(compressed_data)
print("Output:", len(output))

print("Decompressed:", output.decode("utf-8"))

filename = "test.txt.bz2"
compressed_data = bz2.compress(b"this is a test")

try:
    with open(filename, 'wb') as f:
        f.write(compressed_data)
except Exception as e:
    print("Failed to write:", e)

try:
    with open(filename, 'rb') as f:
        recovered_data = f.read()
except Exception as e:
    print("Failed to read:", e)

decompressor = bz2.BZ2Decompressor()
