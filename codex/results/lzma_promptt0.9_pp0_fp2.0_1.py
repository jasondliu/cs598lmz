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
    result.append(decompressor.decompress(s.read()))

print(all(b == result[0] for b in result))
