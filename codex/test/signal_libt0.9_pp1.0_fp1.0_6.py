import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from os.path import join, dirname, abspath

from .core.settings import get_config, create_components, create_argparser
from .core.exceptions import ImproperlyConfiguredError, RequiredKeyError
from .core.logging import log_exception
from .core.utils.misc import to_tuple


def _update_path(cp):
    import sys
    if cp:
        if not cp.startswith(sys.path[0]):
            sys.path.insert(0, cp)

def _update_paths(cps):
    for cp in cps:
        _update_path(cp)


def _import(c_str):
    name = c_str.split('.')[-1]
    mod = __import__(c_str, fromlist=[str(name)])
    klass = getattr(mod, name)
    return klass


