import lzma
# Test LZMADecompressor to decompress some info and then use that output as input for 
#   further decompressions

import sys

def write_to_file(decomp_output):
    """
    decomp_output > Bytes
    """
    with open(sys.argv[2], 'wb') as f:
        if decomp_output.endswith(b'\n'):
            f.write(decomp_output)
        else:
            f.write(decomp_output + b'\n')

def generate_decompression_output(bytes_data, decomp=None):
    """
    bytes_data > Bytes
    decomp > lzma.LZMADecompressor
    """
    if decomp is None:
        decomp = lzma.LZMADecompressor()
    decomp_input = bytes_data
    decomp_output = b''
    decomp_more = True
    while decomp_more:
        decomp_output = decomp_output + decomp.decompress(decomp_input)
        if decomp.eof:
            decomp_more =
