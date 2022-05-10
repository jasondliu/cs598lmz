import lzma
lzma.decompress(_get_lzma_data())

import lzma
lzma.decompress(_get_lzma_data(), format=lzma.FORMAT_AUTO)

import lzma
lzma.decompress(_get_lzma_data(), format=lzma.FORMAT_XZ)

def test_decompressobj():
    import lzma
    lzma.decompressobj().read(b'foo')
    lzma.decompressobj(format=lzma.FORMAT_AUTO).read(b'foo')
    lzma.decompressobj(format=lzma.FORMAT_XZ).read(b'foo')
    with raises(ValueError):
        lzma.decompressobj({"foo": None})
    with raises(ValueError):
        lzma.decompressobj(format=lzma.FORMAT_AUTO, dict_size=10)

def test_decompress_error():
    import lzma
   
