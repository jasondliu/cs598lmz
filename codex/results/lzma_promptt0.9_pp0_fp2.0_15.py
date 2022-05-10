import lzma
# Test LZMADecompressor object

from io import TextIOWrapper

compressor = lzma.LZMACompressor()

text = "Test string 1\nTest string 2".encode('utf-8')
compressed = compressor.compress(text)

print("Compressed: ", compressed)

decompressor = lzma.LZMADecompressor()
output_buffer = decompressor.decompress(compressed)
print("Decompressed:", output_buffer.decode('utf-8'))

print("Excess output:", decompressor.unconsumed_tail)

unused = decompressor.flush()
print("Flushed to: " + unused.decode('utf-8'))

print("Decompressor State: %s" % decompressor.eof)

print("Decomressor Buffer Length: %s" % decompressor.buffered)

print("Compressor State: %s" % compressor.eof)

print("Compressor Buffer Length: %s" % compressor.buffered)

# Test LZMADecompressor context manager closed
