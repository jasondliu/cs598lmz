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

if sys.version_info < (3, 8):
    __all__.extend([
        'PickleBuffer',
        'UnpickleBuffer',
        'PicklerBuffer',
        'UnpicklerBuffer',
        'dump_buffer',
        'load_buffer'
    ])

HIGHEST_PROTOCOL = 5
DEFAULT_PROTOCOL = 0

_compression = {
    1: zlib.compress,
    2: zlib.compress,
    3: zlib.compress,
    4
