import mmap

from . import xtlink
from . import lm
from . import util
from . import fast_align

from .xtlink import XTLinkToken, XTLink
from .lm import LanguageModel, LanguageModelToken
from .util import log_info, log_warn, log_error
from .fast_align import FastAlignToken, FastAlign

def load_xtlink(filename):
    """
    Read XTLink from file
    """
    x = XTLink()
    x.read_file(filename)
    return x

def load_lm(filename):
    """
    Read Language Model from file
    """
    l = LanguageModel()
    l.read_file(filename)
    return l

def load_fastalign(filename):
    """
    Read FastAlign from file
    """
    f = FastAlign()
    f.read_file(filename)
    return f

def mmap_file(filename):
    """
    Memory map a file
    """
    f = open(filename, "r+b")
    return mm
