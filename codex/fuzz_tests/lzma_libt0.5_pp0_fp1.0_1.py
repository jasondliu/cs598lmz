import lzma
lzma.decompress(data)
#b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# This is a much more compact representation!

# The lzma module includes a tool for compressing and decompressing files
# in the LZMA format. For example, suppose we have a large binary file
# in the current directory:

import os
os.chdir('/Users/beazley/Downloads')
os.listdir('.')
#['python-3.3.0.tar.bz2', 'python-3.3.0.tar.bz2.part']

# We can compress this file using the lzma command line tool:

os.system('lzma -z python-3.3.0.tar.bz2')

# This creates a compressed file in the same directory:

os.listdir('.')
#['python-3.3.0.tar.
