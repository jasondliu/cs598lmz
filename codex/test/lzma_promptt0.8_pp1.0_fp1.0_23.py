import lzma
# Test LZMADecompressor objects

def check_valid_data(data):
    raise NotImplementedError

p = lzma.LZMADecompressor()
assert p.unused_data == b""
assert p.eof is False
assert p.needs_input is True

