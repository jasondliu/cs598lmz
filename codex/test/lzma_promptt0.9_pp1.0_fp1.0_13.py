import lzma
# Test LZMADecompressor before using it. Otherwise, it will raise an error if LZMA
# is not supported on the platform.
s = b'\x00\x00\x00\x03\x00\x00\x00\x00\xecUN\x00\x88\x01\x99\x00\x16\x00\x00\x00k\xba\x1e\x1ey\xe0\xf8tA\xaa'
