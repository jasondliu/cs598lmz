import types
types.ModuleType.__dict__.update(dict(
    __file__ = __file__,
    __name__ = __name__,
    __doc__ = __doc__,
    __package__ = __package__,
    __path__ = __path__,
    __loader__ = __loader__,
))

__loader__ = None; del __loader__
__package__ = None; del __package__
__path__ = None; del __path__
