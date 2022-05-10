import io
class File(io.RawIOBase): def write(self, b): pass
try:
    import winreg
except ImportError:
    winreg = None

# Python 2/3 compat
if sys.version_info >= (3,):
    xrange = range
else:
    input = raw_input

def _is_hidden_path(path):
    name = os.path.basename(path)
    return name.startswith('.') or has_hidden_attribute(path)

def is_path_hidden(path):
    """
    Returns ``True`` if the given path is hidden.
    """
    parent_path, name = os.path.split(path)
    return name.startswith('.') or _is_hidden_path(parent_path)

def has_hidden_attribute(filepath):
    try:
        import ctypes
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
       
