import lzma
lzma.decompress(open('enwik8','rb').read())

# If you run this program with "python lzma.py enwik8" as a command line argument,
# it will decompress the file and print the output.
#
# If you run it with "python lzma.py enwik8.xz", it will decompress the .xz file directly
# and print the output.
#
# The .xz format is a single-file compression format that is based on the LZMA2 algorithm.
# It has a higher compression ratio than bzip2.
#
# The file enwik8 is a 100MB text file from Wikipedia.
# The file enwik8.xz is a compressed version of the same file, using xz.
#
# This code is released to the public domain.

import sys
import lzma

if len(sys.argv) == 1:
    sys.exit('Usage: %s FILES...' % sys.argv[0])

for filename in sys.argv[1:]:
    if filename.endswith(
