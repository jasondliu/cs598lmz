import lzma
# Test LZMADecompressor with a truncated stream.
import io
import lzma

data = b'trash ' * 1_000_000
compressed = lzma.compress(data)

decompressor = lzma.LZMADecompressor()
result = []

for i in range(5):
    s = io.BytesIO(compressed[:len(compressed) * i // 5])
