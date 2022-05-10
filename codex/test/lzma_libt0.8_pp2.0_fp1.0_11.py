import lzma
lzma_encode = None
lzma_decode = None
if hasattr(lzma, 'compress'):
    lzma_encode = lzma.compress
if hasattr(lzma, 'decompress'):
    lzma_decode = lzma.decompress
# PyPy
if lzma_encode is None or lzma_decode is None:
    import backports.lzma
    lzma_encode = backports.lzma.compress
    lzma_decode = backports.lzma.decompress


