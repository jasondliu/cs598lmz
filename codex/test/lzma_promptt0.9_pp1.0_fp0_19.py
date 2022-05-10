import lzma
# Test LZMADecompressor, and also test that LZMAError is raised
# when an attempt is made to decompress more than the maximum amount
# of input data (2 GiB).
data_1GiB = b'a' * 2**30
