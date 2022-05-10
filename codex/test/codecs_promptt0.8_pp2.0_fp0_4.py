import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

try:
    import _locale
except ImportError:
    # not available on some platforms
    _locale = None

# Workaround for Jython on OS X: Calling strcoll directly causes a crash
# at bootstrap. We need to use the ctypes implementation instead.
