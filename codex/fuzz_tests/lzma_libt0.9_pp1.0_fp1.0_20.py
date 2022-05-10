import lzma
lzma.open

# These are imports that are not *officially* supported by the Python
# standard library, so these might be portable.  Some of these imports
# only work after certain optional C libraries are installed.
try:
    from os import cpu_count
except:
    from multiprocessing import cpu_count

try:
    from bz2 import BZ2File as bzopen
except:
    from bz2 import BZ2CompressorFile as bzopen

try:
    from lzma import LZMAFile as lzmaopen
except:
    LZMA_SUPPORTED = True
except:
    LZMA_SUPPORTED = False

import gzip

# These imports might be moderately portable?
import sqlite3
import xml.etree.ElementTree

# These imports are standard on recent Linux distributions, but they
# might not be available elsewhere.
try:
    from pwd import getpwuid
except:
    pass

try:
    from grp import getgrgid
except:
    pass

try:

