import lzma
# Test LZMADecompressor.read()
with open("/tmp/x.xz", "rb") as f:
    d = lzma.LZMADecompressor()
    data = d.read(f)
    print(data)

"""
import sys
import lzma

with lzma.open("/tmp/x.xz", "rb") as f:
    file_content = f.read()

print(file_content)
"""
