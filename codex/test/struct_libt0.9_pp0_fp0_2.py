import _struct
from . import utils
from . import platform

__version__ = '0.4.1.dev0'


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class UBFAT(object):
    def __init__(self, fp, autoread=True, align=4096):
        self.fat_read = None
        self._seek = fp.seek
        self._read = fp.read
        self._write = fp.write
        self._tell = fp.tell
        self.fp = fp
        self.align = align
        if autoread:
            self.read()
