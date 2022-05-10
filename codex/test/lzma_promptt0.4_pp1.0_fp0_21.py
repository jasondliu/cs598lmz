import lzma
# Test LZMADecompressor
from lzma import LZMADecompressor
from io import BytesIO

# Test LZMADecompressor
#from lzma import LZMADecompressor
from io import BytesIO

# Test LZMACompressor
from lzma import LZMACompressor
from io import BytesIO

# Test LZMAFile
from lzma import open as lzma_open
from tempfile import TemporaryFile
from os import unlink
from os.path import exists

# Test BZ2File
from bz2 import BZ2File
from tempfile import TemporaryFile
from os import unlink
from os.path import exists

# Test BZ2Compressor
from bz2 import BZ2Compressor
from io import BytesIO

# Test BZ2Decompressor
from bz2 import BZ2Decompressor
from io import BytesIO

# Test GzipFile
from gzip import GzipFile
from tempfile import TemporaryFile
from os import unlink
from os.path import exists

# Test GzipFile
