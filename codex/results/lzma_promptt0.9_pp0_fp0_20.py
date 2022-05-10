import lzma
# Test LZMADecompressor with an LZMA file created with outside the stdlib
# with e.g. 7za ...
path = os.path.join(os.path.dirname(__file__), 'inputs', 'lzma.lzma')
with lzma.open(path) as infile, \
         lzma.LZMADecompressor().open(infile) as un:
    check_decompressor(un)

check_decompressor(lzma.decompress(SMALL_LZMA))
check_decompressor(lzma.decompress(SMALL_LZMA, format=lzma.FORMAT_ALONE))

def check_bad_input(buf):
    try:
        lzma.decompress(buf)
        raise Exception("Decompression should fail but succeeded")
    except ValueError:
        pass

check_bad_input(b"")
check_bad_input(b"ABCDE")
check_bad_input(SMALL_LZMA + b"junk")
check_bad_input
