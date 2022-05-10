import weakref


class DefaultDict(dict):
    def __init__(self, default_factory=None, *args, **kwargs):
        if (default_factory is not None and not callable(default_factory)):
            raise TypeError('first argument must be callable or None')
        dict.__init__(self, *args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            if self.default_factory is not None:
                return self.default_factory()
            raise
    
    def __copy__(self):
        return DefaultDict(self.default_factory, self)
    
    def __deepcopy__(self, memo):
        import copy
        return DefaultDict(self.default_factory, copy.deepcopy(self.items()))
    
    def __repr__(self):
        return dict.__repr__(self)

