fn = lambda: None
# Test fn.__code__ as it's used in the traceback
setattr(fn, '__code__', fn.__code__)
_CODE_ATTRS = tuple(sorted(dir(fn.__code__)))

__all__ = [
    'Error', 'Warning', 'DeprecationWarning', 'PendingDeprecationWarning',
    'RuntimeWarning', 'SyntaxWarning', 'UserWarning', 'FutureWarning',
    'ImportWarning', 'UnicodeWarning', 'BytesWarning', 'ResourceWarning',

    '__debug__',

    'get_debug_queries', 'reset_debug_queries', 'show_debug_backtrace',
    'show_migration_stats',
]


class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass


class Warning(Exception):
    """
    Base class for warnings in this module.
    """
    pass


class DeprecationWarning(Warning):
    """
    Base class for warnings about deprecated features.
    """
    pass


class PendingDeprecationWarning(Warning):
   
