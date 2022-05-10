import lzma
# Test LZMADecompressor
VALID_MULTIPLE = (lambda comp: comp._unconsumed_tail != b'')
INVALID_MULTIPLE = (lambda comp: comp._buffer.getvalue() != b'')
INVALID_SINGLE = (lambda comp: comp.unused_data != b'')
