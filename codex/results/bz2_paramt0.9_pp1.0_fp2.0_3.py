from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(chunk)

BZ2File().read()

from gzip import GzipFile
GzipFile().read()

from lzma import LZMADecompressor
LZMADecompressor().decompress(chunk)

from snappy import SnappyDecompressor
SnappyDecompressor().decompress(chunk)

from zlib import decompress
decompress(chunk)

import codecs
from binhex import binascii
import hashlib
from hmac import HMAC
from numbers import Integral
from pickle import dumps
from struct import pack
from tempfile import mkdtemp
from threading import current_thread
from time import sleep
from xmlrpc.client import ServerProxy
logging.debug('')
logging.info('')
logging.warning('')
logging.error('')
logging.critical('')
logging.getLogger('name')
logging.basicConfig(level=logging.DEBUG)
logging.DEBUG

import logging
FORMAT = '%
