import lzma
# Test LZMADecompressor

print("Testing LZMADecompressor")

decompressor = lzma.LZMADecompressor()

# Test single-shot decompression

print("Single-shot decompression")

data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

outbuf = decompressor.decompress(data)

print("Output buffer: " + str(outbuf))
print("Unused data: " + str(decompressor.unused_data))
print("Need more input: " + str(decompressor.eof))
print("")

# Test multi-shot decompression

print("Multi-shot decompression")

data = b"\x00\x00\x00\x00\x00"

outbuf = decompressor.decompress(data)

print("Output buffer: " + str(outbuf))
