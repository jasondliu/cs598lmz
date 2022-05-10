import gc, weakref

from . import utils
from . import _gdbm_ndbm

try:
    from _gdbm_ndbm import _gdbm as gdbm
except ImportError:
    from _gdbm_ndbm import ndbm as gdbm

__all__ = ["open", "library"]

library = _gdbm_ndbm.__name__

_dbm = gdbm

def open(file, flag='r', mode=0666, open=open):
    """open(file[, flag[, mode]]) -> dbm database.

    Open the database file, where flag can be 'r' (default) for reading,
    'w' for writing, or 'c' for creating.  The file will be created if it
    doesn't exist when opened for writing or creating.  When opened in
    write or create mode, the entire database will be lost if the program
    is interrupted.  The optional argument mode specifies the Unix mode
    of the file, used only when the database has to be created.  It defaults
    to octal code 0666
