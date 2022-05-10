import lzma
# Test LZMADecompressor().remaining_size with corrupt data.

for testno in range(10):
    print("Test", testno)
    if testno in (3, 5, 7, 9):
        cor_contents = b"a"
    else:
        cor_contents = b""
    comp = lzma.compress(b"a" * testno + b"abcdefghijkl")
    comp = comp[:-1] + cor_contents + comp[-1]
    dec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=None)
    try:
        dec.decompress(comp)
    except EOFError:
        print("EOF at byte", dec.unused_data)
