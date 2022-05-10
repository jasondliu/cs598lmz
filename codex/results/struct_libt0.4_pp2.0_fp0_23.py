import _struct
import _thread
import _threading_local
import _warnings
import _weakref
import _weakrefset

# Modules included in the standard library.
# These are all considered "essential" for a functioning Python.
#
# Note that some of these may not actually be built on all platforms.
#
# XXX This list may contain modules that are no longer part of the
# standard library.  Clean up periodically.
_essential_modules = [
    "_abc",
    "_ast",
    "_bisect",
    "_blake2",
    "_codecs",
    "_codecs_cn",
    "_codecs_hk",
    "_codecs_iso2022",
    "_codecs_jp",
    "_codecs_kr",
    "_codecs_tw",
    "_collections",
    "_contextvars",
    "_csv",
    "_datetime",
    "_functools",
    "_heapq",
    "_imp",
    "_io",
    "_json",
    "_locale",
    "_lsprof
