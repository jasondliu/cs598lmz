import lzma
# Test LZMADecompressor.readinto() with files with headers and indexes.
# Padded files don't work right; the LZMA library pads the output to the
# next multiple-of-four bytes.  That may be a bug, or it may be intentional.
