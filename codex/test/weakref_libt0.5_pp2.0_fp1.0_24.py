import weakref

from . import (
    util,
    core,
    geometry,
    types,
    function,
    )

class _Module(object):
    """
    The base class for all modules.
    """
    _c_module = None
    _c_module_name = None
    _c_header_filename = None
    _c_header_string = None
    _c_source_filename = None
    _c_source_string = None
    _c_extra_source_filename = None
    _c_extra_source_string = None
    _c_library_filename = None
    _c_library_string = None
    _c_extra_library_filename = None
    _c_extra_library_string = None

    _cache = weakref.WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        # Return cached instance if possible
        if cls in cls._cache:
            return cls._cache[cls]
