fn = lambda: None
# Test fn.__code__.co_flags
if hasattr(fn, '__code__'):
    USE_BYTES_IN_CODE = not (fn.__code__.co_flags & CO_NOFREE)
# Test fn.func_code.co_flags
elif hasattr(fn, 'func_code'):
    USE_BYTES_IN_CODE = not (fn.func_code.co_flags & CO_NOFREE)
else:
    USE_BYTES_IN_CODE = False
del fn

# Python 2.6 only supports bytes in the code object if you use the -b option
# on the command line, or if you use the -bb option to get warnings about
# str/bytes mismatches.  The latter is by far the most common case, so we
# assume that the user never specified the -b option.
if sys.version_info[:2] == (2, 6):
    USE_BYTES_IN_CODE = False

# Python 3.2 only supports bytes in the code object if you use the -b option
# on the command line
