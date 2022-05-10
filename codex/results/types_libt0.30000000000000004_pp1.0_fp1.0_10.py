import types
types.ModuleType.__dict__.update(dict(
    __file__ = __file__,
    __name__ = __name__,
    __path__ = __path__,
    __doc__ = __doc__,
    __package__ = __package__,
    __loader__ = __loader__,
    __spec__ = __spec__,
))
