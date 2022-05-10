import lzma
# Test LZMADecompressor class
decompressor = lzma.LZMADecompressor()
with open('enwik9.xz', 'rb') as input, \
        open('enwik9.txt', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())
 
import string
import re

# Filenames
filename_input = 'enwik9.txt'
filename_output = 'enwik9_10.txt'

# Limit the input file
limit = 500000
# Initialize the word counter
word_counter = {}

# Use only printable characters
printable = set(string.printable)

# Open the input file
with open(filename_input, 'r') as f:
    # Open the output file
    with open(filename_output, 'w') as f_out:
        # Loop through all the lines
        for i, line in enumerate(f):
            # Stop if we reach
