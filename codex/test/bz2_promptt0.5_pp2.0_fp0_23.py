import bz2
# Test BZ2Decompressor, BZ2Compressor
#
# This example shows how to use the BZ2Compressor and BZ2Decompressor classes
# to compress and decompress data.
#
# The data to compress is taken from stdin, and the compressed data is
# written to stdout.  To decompress, specify the --decompress option.
#
# Example:
#   $ python bz2_file.py < /etc/services | wc -c
#   57626
#   $ python bz2_file.py --decompress < /etc/services.bz2 | wc -c
#   104857
#
# Note that the compressed data is larger than the original!

import sys

if sys.argv[1:] and sys.argv[1] == "--decompress":
    # Decompress from stdin to stdout
    compressor = bz2.BZ2Decompressor()
    with sys.stdin as input, sys.stdout as output:
        while True:
            block = input.read(1024)
