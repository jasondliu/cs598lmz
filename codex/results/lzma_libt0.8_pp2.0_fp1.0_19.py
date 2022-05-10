import lzma
lzma_server = lzma.LZMAFile(infile, mode='r')

while True:
    data = lzma_server.read()
    print(data)

    if not data:
        break

    # Send an HTTP header, specifying the content type and the length.
    if not data:
        break

    sys.stdout.write(data)
    sys.stdout.flush()

lzma_server.close()
</code>
I can also get the data from another machine using this code:
<code>#!/usr/bin/env python3
#
# Read data from stdin, compressed by the LZMA library.
#

import lzma
import sys

# Open the compressed file on stdin.
lzma_stream = lzma.LZMAFile(sys.stdin, mode='r')

# Read and write data until the end of the file.
while True:
    data = lzma_stream.read()
    if not data:
        break
    # Send an HTTP header, specifying the content type and
