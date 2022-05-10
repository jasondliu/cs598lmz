import lzma
# Test LZMADecompressor to make sure it's working properly.
# If this test fails, LZMA compression will be disabled.
if hasattr(lzma, 'LZMADecompressor'):
    try:
        lzma.LZMADecompressor().decompress(b'\x00'*10)
    except Exception:
        del lzma
else:
    del lzma

if not hasattr(lzma, 'LZMADecompressor'):
    # Try to use backport
    try:
        from backports import lzma as lzma2
    except ImportError:
        lzma2 = None
    else:
        if hasattr(lzma2, 'LZMADecompressor'):
            lzma = lzma2

if not hasattr(lzma, 'LZMADecompressor'):
    # LZMA compression disabled
    lzma = None
    if not hasattr(bz2, 'BZ2Decompressor'):
        # No compression available
        raise RuntimeError
