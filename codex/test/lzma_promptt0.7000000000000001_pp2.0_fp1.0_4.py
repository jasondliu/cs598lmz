import lzma
# Test LZMADecompressor
import sys
import os
import io

# ---
# This is a utility module for making sure the LZMADecompressor works as expected
# ---
# Inputs:
#   filename (string): name of the file to test
#   max_size (int): maximum number of bytes to read from the file
#   n_blocks (int): number of blocks to use in testing
#   n_threads (int): number of parallel threads
#   decomp_dict_size (int): size of the decompression dictionary to use (0 is default)
# ---
# Outputs:
#   f_decomp_data[i] (bytes): the decompressed data in block i
#   f_decomp_size[i] (int): the size of the decompressed data in block i
def test_decompressor(filename, max_size, n_blocks, n_threads, decomp_dict_size):
    # Open file
    f = open(filename, 'rb')
    f_data = f.read(max_size)
    f.close()
