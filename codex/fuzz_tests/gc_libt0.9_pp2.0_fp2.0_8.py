import gc, weakref
import subprocess, threading
import faulthandler
import code
from cStringIO import StringIO
import traceback
import signal
from util import *


def debugger_this_thread():
    """Spawn a debugger for the current thread. Tries pdb, then ipython."""
    log.debug("starting debugger for this thread")

    # just in case
    gc.collect()

    # try pdb first
    t = threading.current_thread()
    try:
        from pdb import Pdb, bdb
    except ImportError:
        log.warn("pdb not found")
        return

    stdout = sys.stdout

    try:
        import pyreadline as readline
    except ImportError:
        try:
            import readline
        except ImportError:
            readline = None

    stdin = sys.stdin
    sys.stdout = sys.stderr = stdin
    try:
        pdb = Pdb(stdin=stdin)
        _bdb = bdb.Bdb(skip=['newthread', '
