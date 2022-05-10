import lzma
# Test LZMADecompressor.eof functionality, variants of it found in
# zipfile.py and tarfile.py which are known to halt at lzma.LZMAError.

def test_decompressor_eof_not_set(capfd, tmpdir):
    lzf = lzma.LZMADecompressor()

    # write EOF marker a few times
    compressed = lzma.compress(b'foobar', format=lzma.FORMAT_ALONE,
                               check=lzma.CHECK_NONE, eof=lzma.LZMA_FINISH,
                               filters=[{'id': lzma.FILTER_X86}])
    for i in range(4):
        compressed += compressed

    with tmpdir.join("test_decompressor_eof_not_set.bin") as output:
        with open(output, 'wb') as outfile:
            outfile.write(compressed)

        with open(output, 'rb') as infile:
            out = lzf.decompress(infile.read
