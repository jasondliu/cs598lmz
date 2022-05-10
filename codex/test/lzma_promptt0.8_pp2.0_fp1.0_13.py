import lzma
# Test LZMADecompressor and LZMACompressor classes

lzc = lzma.LZMACompressor()
ctext = lzc.compress(b"Spam, spam, spam, spam, spam, " * 10)
ctext += lzc.flush()
print("Original length:", len(ctext))

lzd = lzma.LZMADecompressor()
result = lzd.decompress(ctext)
print("Result:", result)

print("Needed bytes:", lzd.unused_data)
print("Needed data length:", len(lzd.unused_data))

lzd = lzma.LZMADecompressor()
more_result = lzd.decompress(lzd.unused_data)
print("More Result:", more_result)

print("Needed bytes:", lzd.unused_data)
print("Needed data length:", len(lzd.unused_data))

