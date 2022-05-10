import gc, weakref

from lupa import LuaRuntime, LuaError
from uzbl.plugins.lua import _wrap_file_object

import uzbl

def _parse_dict(d):
    return dict((k, v.split('\n'))
        for k, v in d.iteritems())

def norm_path(path):
    path = os.path.normcase(os.path.normpath(path))
    if os.path.splitdrive(path)[0]:
        path = os.path.splitdrive(path)[1]
    return path

class UzblController(object):
    def __init__(self):
        self._uzbls = set()
        self._uzbls_by_pid = {}
        self._uzbls_by_fd = {}

    def add_uzbl(self, uzbl):
        self._uzbls.add(uzbl)
        if uzbl.pid:
            self._uzbls_by_pid[uzbl.pid] = uzbl

        if uzbl is sys.stdin
