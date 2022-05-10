import io
# Test io.RawIOBase
from io import RawIOBase
from io import BufferedIOBase
from io import BufferedReader
from io import BufferedWriter
from io import BufferedRWPair
from io import BytesIO
from io import StringIO
from io import TextIOWrapper
from io import TextIOBase
# Test io.FileIO
from io import FileIO

from io import __all__ as io_all
from io import DEFAULT_BUFFER_SIZE, SEEK_CUR, SEEK_END, SEEK_SET

from io import UnsupportedOperation
from io import BlockingIOError
