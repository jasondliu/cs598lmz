from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# bz2.open()
# bz2.open() is a convenience function for opening bzip2-compressed files.
# It accepts the same arguments as the built-in open() function,
# but it uses an instance of BZ2File as the file object.

# bz2.open() is a convenience function for opening bzip2-compressed files.
# It accepts the same arguments as the built-in open() function,
# but it uses an instance of BZ2File as the file object.

# For example:

with bz2.open('file.bz2', 'wt') as f:
    f.write('Contents of the example file go here.\n')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# The bz2.open() function is only available in Python 3.
# In Python 2, use the bz2file module.

# For example:

import bz2file
with bz2file.open
