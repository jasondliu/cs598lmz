import ctypes
ctypes.cast(id(w_obj), ctypes.py_object).value

#TestVar
#%%%text
import sys, types, locale
from .dist import get_localedir
default_encoding = locale.getpreferredencoding()
try:
    default_encoding = sys.getdefaultencoding()
except AttributeError:
    pass

def isreadable(filename):
    #There may be a problem with unicode type directory name.
    from . import dist
    if dist.is_jython:
        filename = filename.encode(default_encoding)
        return os.access(filename,'r')
    try:
        fd = os.open(filename, os.O_RDONLY)
    except OSError:
        return False
    else:
        os.close(fd)
        return True

def iswritable(filename):
    #There may be a problem with unicode type directory name.
    from . import dist
    if dist.is_jython:
        filename = filename.encode(default_encoding)
        return os.
