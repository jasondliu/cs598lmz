import lzma
lzma.LZMACompressor

# compress data
compressor = lzma.LZMACompressor(format=lzma.FORMAT_RAW)
compressed = compressor.compress(data)
compressed += compressor.flush()

# decompress the data with lzma
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# display the compressed and decompressed data sizes
print(f"Original: {len(data)} bytes")
print(f"Compressed: {len(compressed)} bytes")
print(f"Decompressed: {len(decompressed)} bytes")

# show the ratio of compression
print(f"Compressed {len(data) / len(compressed):.2f} times")

# check that the data is the same
try:
  print(f"Same: {data == decompressed}")
except:
  print(f"Compressed:")
  print(compressed)
  print(f"Decompressed:")
  print(decomp
