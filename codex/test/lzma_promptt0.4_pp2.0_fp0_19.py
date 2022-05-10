import lzma
# Test LZMADecompressor

import lzma
import io

input_data = b"".join(
    [bytes([x]) * x for x in range(256)] * 100
)

compressor = lzma.LZMACompressor()
compressed = io.BytesIO()
compressed.write(compressor.compress(input_data))
compressed.write(compressor.flush())
compressed.seek(0)

decompressor = lzma.LZMADecompressor()
decompressed = io.BytesIO()
decompressed.write(decompressor.decompress(compressed.read()))
decompressed.seek(0)

print(len(input_data))
print(len(compressed.getvalue()))
print(len(decompressed.getvalue()))

assert input_data == decompressed.getvalue()

# Test LZMADecompressor.decompress()

import lzma

