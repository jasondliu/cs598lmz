import _struct
from . import bloscpack_meta
from . import version

# On Windows, raise an exception if the file is opened in text mode.
if sys.platform == 'win32':
    import os, msvcrt
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stderr.fileno(), os.O_BINARY)


BLOSC_VERSION_FORMAT = _struct.Struct('<i')

# Serialization constants
FORMATS = {'pickle': 1}
FORMAT_NAMES = {'pickle': 'Python Pickle'}
FORMAT_DESCRIPTIONS = {'pickle': 'Serialize Python object using Python Pickle format.'}

# Metadata constants
EXPECTED_BLOSC_VERSION = (1, 3, 0)

def _write_metadata(f, blosclz_level, clevel, shuffle
