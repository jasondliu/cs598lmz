import bz2
bz2.BZ2Compressor()

try:
    import png
except ImportError:
    png = None

try:
    import tiff
except ImportError:
    tiff = None

try:
    import jpeg
except ImportError:
    jpeg = None

try:
    from sample_data import large_binary_data
except ImportError:
    large_binary_data = None

from pypy.rpython.lltypesystem import lltype, llmemory
from pypy.rpython.ootypesystem import ootype
from pypy.rpython.rbuiltin import execfile
from pypy.rlib.rarithmetic import intmask
from pypy.rlib.rstring import ParseStringError, SearchStringError
from pypy.tool.udir import udir
from pypy.translator.c.test.test_genc import compile
from pypy.translator.translator import TranslationContext
from pypy.translator.unsimplify import varoftype


def test_auto_promotion():
    inf
