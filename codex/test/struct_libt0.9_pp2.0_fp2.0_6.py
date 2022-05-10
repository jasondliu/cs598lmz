import _struct
import _compression
from _compression import ZStdError, ZStandardError

from blosc.reallib import reallib
import blosc.compressor
from blosc.util import ColorText, timet
from blosc.utils import *


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_reallib import check_reallib_available
from test_reallib import check_compressor_available  # @UnusedImport
from test_reallib import check_blo_arguments  # @UnusedImport


# Default compression parameters
# _clevel   = 1       # compression level
_cname    = 'blosclz'    #
_shuffle  = 'none'   # shuffle mode
_blocksize = 0
_nthreads = 0
_typesize = 1

_verbose = 0  # verbose mode

_colortext = ColorText()
