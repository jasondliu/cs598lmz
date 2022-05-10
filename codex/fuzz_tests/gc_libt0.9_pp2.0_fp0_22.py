import gc, weakref, operator, logging
from fnmatch import fnmatch  # fnmatchcase is _really_ slow
from collections import defaultdict
from . import hist
from .filterparser import get_filter
from . import lam
from .defaults import default_filter
from .repr_record import repr_record
from .reported import Reported
from . import pool
from .importor import import_

log = logging.getLogger(__name__)

def stamp(value=None):
    return hist.Histogram(value=value)
def stitch(): return hist.stitch()

def push(record):
    global_hists = _global_hists()
    for keyed_hist in global_hists:
        keyed_hist.push(record)

def plot(*args, **kwargs):
    hists = _global_hists()
    hists.extend(args)
    hists.plot(**kwargs)

def root(*args, **kwargs):
    return _global_hists().root(*args, **kwargs)

def report():
    return _global
