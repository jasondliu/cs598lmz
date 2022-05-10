import bz2
# Test BZ2Decompressor
data = bz2.BZ2Compressor().compress(b"Hello World!")
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
result
# Test BZ2File
import bz2
# Write compressed data to a file
data = b"Lots of content here."
with bz2.BZ2File("file.txt.bz2", "wb") as f:
    f.write(data)
# Read compressed data from a file
import bz2
with bz2.BZ2File("file.txt.bz2", "rb") as f:
    file_content = f.read()
file_content
# Test bz2.open()
import bz2
data = b"Lots of content here."
with bz2.open("file.txt.bz2", "wb") as f:
    f.write(data)
import bz2
