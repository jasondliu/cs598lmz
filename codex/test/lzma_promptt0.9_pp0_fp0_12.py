import lzma
# Test LZMADecompressor
# Example from http://python-lzma.python.narkive.com/
# And from http://bugs.python.org/issue11395


###############################################################################
# Prepare data

# The data passed must be bytes-like, either a bytes instance or an object
# exposing the buffer interface (such as a bytearray).
# The data passed must be bytes-like, either a bytes instance or an object
# exposing the buffer interface (such as a bytearray).
#
list_of_bytes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

with open('tmp.lzma', 'wb') as fout:
    with lzma.open(fout, 'wb') as xzout:
        xzout.writelines([int(x).to_bytes(1, 'little') for x in list_of_bytes])

