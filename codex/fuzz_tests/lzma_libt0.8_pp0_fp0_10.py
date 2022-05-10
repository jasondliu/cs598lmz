import lzma
lzma.LZMA.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\xff\xfb\x52\x44\x53\x5a\x58\x56\x00\x10\x34\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# decompress LZMA files
import lzma
lzma.LZMAFile(open('archive.xz', 'rb'))

# calculate the length of a file
import os
os.path.getsize('file_path')

# calculate the length of a file in reading/writing mode
import os
os.fstat(0).st_size

# read the last byte of a file
with open('file_path', 'rb') as f:
    f.seek(-1,
