import lzma
# Test LZMADecompressor to see if LZMA compression is available.
try:
    z = lzma.LZMADecompressor()
except:
    lzma = None


__all__ = [
    'Sqlite3Unpickler',
    'BadPickleGet',
    'Pickler',
    'Unpickler',
    'dump',
    'dumps',
    'load',
    'loads',
    'HIGHEST_PROTOCOL',
    'DEFAULT_PROTOCOL'
]

