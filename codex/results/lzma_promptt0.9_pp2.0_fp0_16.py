import lzma
# Test LZMADecompressor class

print("Data format:  Python data structure ({0} bytes) -> pickle({1} "
      "bytes) -> XZ({2} bytes) -> Python data structure back\n"
      .format(len(xs), len(pickle.dumps(xs)), len(lzma.compress(pickle.dumps(xs)))))

decompressor = lzma.LZMADecompressor()

data = pickle.dumps(xs)
print("Input size:", len(data))

compressed = lzma.compress(data)
print("Compressed size:", len(compressed))

# Test LZMADecompressor.decompress
decompressed = decompressor.decompress(compressed)
decompressed = pickle.loads(decompressed)
assert xs == decompressed
print("Decompressed OK")

# Test LZMADecompressor.flush
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
dec
