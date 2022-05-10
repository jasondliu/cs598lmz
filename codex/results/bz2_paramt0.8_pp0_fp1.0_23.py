from bz2 import BZ2Decompressor
BZ2Decompressor()
from json import JSONDecoder
JSONDecoder()
from gzip import GzipFile
GzipFile(name='', mode='', fileobj=None, compresslevel=9)
from tarfile import TarFile
TarFile(name='', mode='', fileobj=None, format=None, tarinfo=None, dereference=False, ignore_zeros=False, encoding=None, errors=None, pax_headers=None, debug=0, errorlevel=0, strict_gnu=False)
from zlib import decompress, compress
decompress(data=None)
compress(data=None)
from hashlib import md5, sha1, sha256, sha512
md5(data=None)
sha1(data=None)
sha256(data=None)
sha512(data=None)
from random import SystemRandom
SystemRandom()
from urllib.parse import urlparse, urljoin, parse_qsl, urlencode
urlparse(url=None)
urljoin(base=None, uri=None)
parse_qsl(qs=None)

