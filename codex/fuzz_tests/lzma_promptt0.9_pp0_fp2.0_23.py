import lzma
# Test LZMADecompressor
from io import BytesIO
test = b'\x00\x10\x00\x00\x00\x01\x00\x00\x00\x01'
decompressor = lzma.LZMADecompressor()
decompressor.decompress(test)

# Output to bytes.io
output = BytesIO()

# Input File
with lzma.open("lzma/input/compressed.xz", "rb") as f:
    with open("lzma/output/decompressed.log", "w") as file:
        while True:
            chunk = f.read(16384)
            if not chunk:
                break
            file.write(decompressor.decomp
