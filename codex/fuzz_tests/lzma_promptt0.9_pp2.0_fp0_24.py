import lzma
# Test LZMADecompressor - decompress multiple files.
# The command line should be:
#    test_lzma.py compression1 compression2...
# For example:
#    test_lzma.py bz2 lzma zlib
# It's also possible to change values of chunk sizes.
# decompressor specific keyword arguments, e.g.
#    test_lzma.py --format xz --check sha256 zlib
# To get a full list of supported options, run:
#    test_lzma.py -h

operation = "decompress"

# Comma separated list of supported 
