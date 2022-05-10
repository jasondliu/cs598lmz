from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile(fileobj=StringIO('a'))

from lzma import LZMADecompressor
LZMADecompressor()

from zlib import decompress
decompress('a')


# ___________________________________________________________________________
# test_datetime

from datetime import datetime
datetime.now()

from datetime import timedelta
timedelta(days=1)

from datetime import tzinfo

class TZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1)

TZ()


# ___________________________________________________________________________
# test_dbm

from dbm.ndbm import ndbm
ndbm.open('a', 'c')

from dbm.gnu import gnu
gnu.open('a', 'c')

from dbm.dumb import dumb
dumb.open('a', 'c')


# ___________________________________________________________________________
# test_difflib

from difflib import get_close_matches
get
