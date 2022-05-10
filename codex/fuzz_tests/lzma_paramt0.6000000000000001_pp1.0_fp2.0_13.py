from lzma import LZMADecompressor
LZMADecompressor.create_decompress_pipe = create_decompress_pipe

import sys

# If we don't have a file, quit.
try:
    filename = sys.argv[1]
except IndexError:
    sys.exit(1)

# Open the file
with open(filename, 'rb') as f:
    file_content = f.read()

# Start the decompressor
decompressor = LZMADecompressor()

# Feed in the whole file and close the pipe,
# allowing lzma to notice that it's received
# all of the input it's going to get.
decompressor.decompress(file_content)
decompressor.flush()
