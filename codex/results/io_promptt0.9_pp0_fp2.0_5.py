import io
# Test io.RawIOBase class
# Used by IOBase
class RawIO:
    """descriptor for RawIO objects"""

    def __init__(self, name, default_raw_methods, *methods, **kwargs):
        self.initialized = False
        self.name = name
        # needed to support pickling
        self.default_raw_methods = default_raw_methods
        self.methods = methods
        self.raw_prefix = kwargs.get('raw_prefix') or 'raw_'
        self.incorrect_suffix = kwargs.get('incorrect_suffix',[])
        self.constructor = kwargs.get('constructor',self._default_constructor)

    def _default_constructor(self, io_obj):
        io_obj.initialized = True

    def __set__(self, obj, val):
        if val is None:
            raise AttributeError(
                "can't delete " + self.name + " attribute")
        elif self.initialized:
            raise AttributeError(
                "cannot set "
