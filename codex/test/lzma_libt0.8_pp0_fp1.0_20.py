import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    import lzma
    lzma_compress = lzma.compress
except ImportError:
    try:
        import pylzma
        lzma_compress = pylzma.compress
    except ImportError:
        lzma_compress = None

try:
    import lzma
    lzma_decompress = lzma.decompress
except ImportError:
    try:
        import pylzma
        lzma_decompress = pylzma.decompress
    except ImportError:
        lzma_decompress = None
