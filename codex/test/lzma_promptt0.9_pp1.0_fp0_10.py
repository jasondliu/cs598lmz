import lzma
# Test LZMADecompressor().remaining_size with corrupt data.

for testno in range(10):
    print("Test", testno)
    if testno in (3, 5, 7, 9):
        cor_contents = b"a"
    else:
        cor_contents = b""
    comp = lzma.compress(b"a" * testno + b"abcdefghijkl")
