import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
lzma_compressLevel = lzma.PRESET_EXTREME
if hasattr(lzma, "LZMA_VERSION_NUMBER"):
	lzma_version = lzma.LZMA_VERSION_NUMBER
else:
	lzma_version = 2

try:
    import pyximport
    pyximport.install(setup_args={"include_dirs": numpy.get_include()})
except ImportError:
    print("Loading Cython-compiled modules failed.", file=sys.stderr)

from ..vector import outer1d, outer1d_u
from .table import MetaTable, Table, Record, Column
from .column import DataColumn, ColumnList, ReferenceColumn
from .formats import BinaryFormat, TextFormat
from .formats.binary import BinaryRecord, BinaryTable
from .formats.text import TextRecord, TextTable
from .fits import FitsRecord, FitsTable, FitsColumn

