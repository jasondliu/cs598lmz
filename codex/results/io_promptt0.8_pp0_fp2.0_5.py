import io
# Test io.RawIOBase instead of io.BytesIO?
import numpy as np

from rasterio._io import BufferedReaderBase
from rasterio._io import MemoryFile
from rasterio._io import MemoryFileManager
from rasterio.dtypes import uint8, uint16, uint32, int16, int32, float32, float64
from rasterio.dtypes import uint64, int64
from rasterio.dtypes import complex64, complex128
from rasterio.dtypes import invalid_type_msg
from rasterio.dtypes import dtype_ranges
from rasterio.errors import DataTypeError

TEST_FILE = 'TEST.TIF'

datasets = (
    'tests/data/RGB.byte.tif',
    'tests/data/float.tif',
    'tests/data/float_nan.tif',
    'tests/data/float_alpha.tif',
)

def test_rawiobase():
    """Creates a BytesIO object, confirms that RawIOBase methods
    are available for it, and returns it. 
