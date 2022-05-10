import _struct
from os import _exit as _real_exit

try:
    import faulthandler
except ImportError:
    # faulthandler may not be available on some non-CPython platforms
    faulthandler = None

# This is defined in CPython's pystate.h
Py_TPFLAGS_HAVE_CHANGED = 131072

original_excepthook = sys.excepthook


# NOTE: see bpo-30871
def _excepthook(*args):
    sys._excepthook(*args)
    original_excepthook(*args)


# The original sys.exit() routine.
_sys_exit = sys.exit


# NOTE: see bpo-30871
def _exit(status=0, *args, **kwargs):
    if args or kwargs:
        msg = 'sys.exit() does not accept arguments'
        if PY2:
            msg = buffer(msg)
        raise TypeError(msg)
    raise SystemExit(status)


project_
