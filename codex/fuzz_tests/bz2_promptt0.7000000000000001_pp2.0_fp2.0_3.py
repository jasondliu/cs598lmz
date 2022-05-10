import bz2
# Test BZ2Decompressor
#
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#

import dlib
import bz2
import sys

if len(sys.argv) != 3:
    print("You must give two command line arguments. The first is the name of the bz2 file, the second is the name of the output file.")
    exit()

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# decompress the data using bz2
print("Reading bz2 compressed file",input_filename)
f = dlib.data_file(input_filename)
print("Writing decompressed file to",output_filename)
file = open(output_filename, 'wb')
decompressor = bz2.BZ2Decompressor()
for block in iter(lambda : f.read(100 * 1024), b''):
    file.write(decompressor.decompress(block))
file.close()
