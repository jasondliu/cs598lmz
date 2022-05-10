import lzma
# Test LZMADecompressor. Before Python-3.7, the LZMAError exception was raised
# for an invalid input.
try:
    lzma.LZMADecompressor().decompress(b"")
except lzma.LZMAError:
    HAS_LZMA = True
else:
    HAS_LZMA = False

# In Python-3.5, we can use tqdm to get the progress bar(requires tqdm>=4.14).
# In Python-3.6, tqdm < 4.14 supported has a different interface.
# In Python-3.7, tqdm >= 4.14 is not supported(it doesn't have 'file' param).
try:
    import tqdm
except ImportError:
    has_tqdm = False
else:
    has_tqdm = True
    try:
        tqdm_version = tuple(map(int, tqdm.__version__.split(".")[:3]))
    except (TypeError, ValueError):
        has_tqdm = False
