import bz2
bz2.BZ2File
import gzip
gzip.GzipFile
import lzma
lzma.LZMAFile
import zipfile
zipfile.ZipFile
import tarfile
tarfile.TarFile

# crypto
import hashlib
hashlib.md5
import hmac
hmac.HMAC
import secrets
secrets.token_bytes
import sys
sys.hash_info
import zlib
zlib.compress

# ctypes
import ctypes
ctypes.c_long
import ctypes.util
ctypes.util.find_library

# datetime
import datetime
datetime.date
import datetime.tzinfo
datetime.tzinfo.UTC

# decimal
import decimal
decimal.Decimal

# doctest
import doctest
doctest.DocTestFinder
import doctest.DocTestFinder
doctest.DocTestFinder.find
import doctest.DocTestParser
doctest.DocTestParser.parse
import doctest.OutputChecker
doctest.OutputChecker.check_output
import doct
