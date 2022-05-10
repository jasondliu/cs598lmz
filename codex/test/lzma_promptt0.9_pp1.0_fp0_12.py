import lzma
# Test LZMADecompressor with given input and if output is
# the same with lzmadec.
def test_lzma_decompressor(seq):
    c = lzma.LZMADecompressor()
    arg = b''.join(seq)
    lzmadc_out = get_lzmadc_output(arg)
    decomp_out = []
    while True:
        out = c.decompress(arg)
        if out:
            decomp_out.append(out)
        elif not c.eof:
            raise ValueError('LZMADecompressor.eof but no output')
        else:
            break
    if b''.join(decomp_out) != lzmadc_out:
        print('LZMADecompressor gives incorrect output, giving up.')
        print(lzmadc_out)
        print(b''.join(decomp_out))
        raise ValueError()
    return decomp_out

# Make random snippets of data, with a minimum size.
# The distribution of sizes is skewed to favor more
# small
