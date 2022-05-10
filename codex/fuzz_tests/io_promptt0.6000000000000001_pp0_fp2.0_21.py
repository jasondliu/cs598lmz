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
from io import InterruptedError
from io import UnsupportedOperation
from io import BlockingIOError
from io import InterruptedError

from io import open as iopen
from io import __doc__ as iodoc

from io import TextIOWrapper as cTextIOWrapper
from io import BytesIO as cBytesIO
from io import StringIO as cStringIO

from io import FileIO as cFileIO

from io import BufferedWriter as cBufferedWriter
from io import BufferedReader as cBuff
