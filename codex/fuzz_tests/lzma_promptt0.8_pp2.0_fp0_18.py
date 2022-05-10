import lzma
# Test LZMADecompressor

def test_lzmadecomp():
    
    cdata = lzma.LZMACompressor().compress(b"lzma")
    cdata += lzma.LZMACompressor().flush()
    
    decomp = lzma.LZMADecompressor()
    
    
    data = decomp.decompress(cdata)
    if decomp.unused_data:
        raise ValueError
    assert data == b"lzma"
    
    
def test_lzmadecomp_unused_data():
    """Test if unused_data is properly stored when fed in parts"""
    
    cdata = lzma.LZMACompressor().compress(b"lzma")
    cdata += lzma.LZMACompressor().flush()
    assert len(cdata) > 8
    cdata = cdata[:8]
    
    decomp = lzma.LZMADecompressor()
    
    
    data = decomp.decompress(cdata,1)
    assert data == b"
