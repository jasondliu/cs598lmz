import lzma
# Test LZMADecompressor object
# input and output based on strings

TEST_DATA = [
    b"This is the test case for LZMADecompressor!", # last byte is index of lc/lp/pb to use
    b"x\x9cKJ\x01\x04\x00\x11\x00"   # compress 1 byte
    b'abcdabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcd', # compress 33 * 65 bytes
    b'a' * 128 + b'b' * 128 + b'c' * 128 + b'd' * 129, # compress 128 + 128 + 128 + 129 bytes
    b'\x00' * 64 + b'\x00' * 64 + b'\x00' * 64 + b'\x00' * 65, # compress 64 + 64 + 64 + 65 bytes
    b'\xff' * 64 + b'\xff' * 64 + b'\xff' * 64 + b'\xff' * 65, # compress 64 + 64 + 64 +
