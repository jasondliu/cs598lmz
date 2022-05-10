import threading
threading_available = True
except ImportError:
    threading_available = False

try:
    from collections import OrderedDict
    ordered_dict_available = True
except ImportError:
    ordered_dict_available = False

import re


if threading_available:
    class ThreadingCache(threading.local, dict):
        pass
else:
    class ThreadingCache(dict):
        pass


_glob_match_cache = ThreadingCache()
_re_compile_cache = ThreadingCache()

_re_symbols_re = re.compile(r'[\+\*<>\[\]=\(\){}\?\-\^&\$|\.]')
_is_glob_symbol = lambda symbol: _re_symbols_re.search(symbol)


def _format_path(path):
    return path.rstrip('/')


class FileSystemPath(object):
    """
    Light wrapper around a path string.

    """

    def __init__(self, path):
        self._path
