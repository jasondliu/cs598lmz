fn = lambda: None
# Test fn.__code__ for Python 2.4 compatibility
_identifier_re = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')


class _LazyDescr(object):
    """Lazy descriptor.
  
    Descriptor that calls a given callable *fn* the first time it is called,
    and replaces itself with the result of that call, called with no
    arguments.
    """
    def __init__(self, fn):
        self._fn = fn
        try:
            self.__doc__ = fn.__doc__
        except AttributeError:
            pass

    def __get__(self, inst, cls):
        value = self._fn()
        setattr(cls, self.__name__, value)
        return value


class _ModuleMarker(object):
    """Attribute holder for module globals"""


class _LazyModule(types.ModuleType):
    """Lazy module.
  
    Implements lazy loading of submodules and attributes.
    """
    def __init
