import lzma
# Test LZMADecompressor
import io

output = io.BytesIO()
with lzma.open("foo.xz", "wb") as f:
    f.write(b"contents of the original file")

with lzma.open("foo.xz") as f:
    file_content = f.read()

print(file_content)
with open("foo.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    s = decompressor.decompress(f.read())
    print(s)

with open("foo.xz", "rb") as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b""):
        decompressor.decompress(chunk)
 
    remaining = decompressor.decompress(b"")
    print(remaining)
    remaining += decompressor.flush()
    print(remaining)
