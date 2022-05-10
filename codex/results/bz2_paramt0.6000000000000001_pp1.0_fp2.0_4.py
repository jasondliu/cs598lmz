from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

# example
from bz2 import BZ2File
with BZ2File('file.bz2') as f:
    file_content = f.read()

# example
import bz2
compressed_file = bz2.decompress(compressed_file)

# example
import bz2
with open('file.txt', 'rb') as f:
    file_content = f.read()
with open('file.bz2', 'wb') as f:
    f.write(bz2.compress(file_content))

# example
import bz2
with open('file.bz2', 'rb') as f:
    file_content = bz2.decompress(f.read())
with open('file.txt', 'wb') as f:
    f.write(file_content)
