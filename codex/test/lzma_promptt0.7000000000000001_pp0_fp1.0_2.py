import lzma
# Test LZMADecompressor's ability to decompress a chunk at a time.
def test_partial_decompression():
    data = b'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
    comp = lzma.compress(data)
    for chunk_size in range(1, len(comp)):
        decomp = lzma.LZMADecompressor()
        for i in range(0, len(comp), chunk_size):
            chunk = comp[i:i+chunk_size]
            res = decomp.decompress(chunk)
            assert res == data[i:], i
        assert decomp.decompress() == b''
        assert decomp.unused_data == b''
        decomp = lzma.LZMADecompressor()
        res = decomp.decompress(comp)
        assert res == data
        assert decomp.unused_data == b''
        decomp = lzma.LZMADecompressor()
        res = decomp.decompress(comp[:len(comp)//2])
        res += decomp
