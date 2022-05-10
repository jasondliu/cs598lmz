import lzma
lzma_preset = getattr(lzma, 'FORMAT_XZ', None)
del lzma
import tokenize
pyc_magic_int = getattr(imp, 'get_magic', None) and imp.get_magic()
del imp
try:
    import winreg as _winreg
except ImportError:
    import _winreg

try:
    import locale
    stdout_isatty = sys.stdout.isatty()
except Exception:
    stdout_isatty = False

def get_all_read_codes():
    """Return a dict mapping all read codes to their names"""
    codes = {}
    for name in dir(tokenize):
        if name.startswith('ERRORTOKEN_'):
            value = getattr(tokenize, name)
            if isinstance(value, int):
                codes[value] = name
    return codes

def pyc_magic_is_threaded():
    """Return whether a pyc file would have a threaded magic value"""
    return pyc_magic_int and pyc
