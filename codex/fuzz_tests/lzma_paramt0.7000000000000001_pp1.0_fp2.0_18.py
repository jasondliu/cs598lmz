from lzma import LZMADecompressor
LZMADecompressor.decompress

from io import BytesIO

from gzip import GzipFile, GzipFile
GzipFile.read

from bz2 import BZ2Decompressor
BZ2Decompressor.decompress

from zlib import decompress
decompress

# ------------------------------------------------------------------------------

from bz2 import compress
compress

from lzma import LZMACompressor
LZMACompressor.compress

from zlib import compress
compress

from gzip import GzipFile, GzipFile
GzipFile.write

# ------------------------------------------------------------------------------

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.primitives.ciphers.modes
