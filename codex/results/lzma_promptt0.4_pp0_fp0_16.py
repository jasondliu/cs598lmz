import lzma
# Test LZMADecompressor
#
# This script will decompress a file using LZMADecompressor,
# and compare the results to the output of the xz command-line tool.
#
# Usage:
#
#     python test_lzma.py <file>

import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: test_lzma.py <file>")

filename = sys.argv[1]

# Decompress with LZMADecompressor

with open(filename, "rb") as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read()
    assert decompressor.decompress(data) == b"foo\n"
    assert decompressor.unused_data == b""
    assert not decompressor.eof

# Decompress with xz

with open(os.devnull, "wb") as devnull:
    with open(filename, "rb") as f:
        xz_process = subprocess.Popen(["
