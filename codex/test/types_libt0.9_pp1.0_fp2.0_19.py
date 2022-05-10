import types
types.ModuleType.__repr__ = lambda m: ''  # type: ignore
types.ModuleType.__name__ = lambda m: ''  # type: ignore


