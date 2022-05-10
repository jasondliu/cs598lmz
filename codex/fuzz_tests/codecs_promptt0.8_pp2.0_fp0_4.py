import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

try:
    import _locale
except ImportError:
    # not available on some platforms
    _locale = None

# Workaround for Jython on OS X: Calling strcoll directly causes a crash
# at bootstrap. We need to use the ctypes implementation instead.
try:
    import ctypes
    if '__JYTHON__' in sys.builtin_module_names:
        def strcoll(string1, string2):
            if not isinstance(string1, str) or not isinstance(string2, str):
                raise TypeError
            return ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')).strcoll(string1, string2)
except (ImportError, OSError):
    pass

# When strcoll encounters an error, the global error handler is
# called with a string encoding the exception information; this
# string is then re-raised.  The error codes produced in this way
# are all negative.

def _decode_locale_error(exc):
