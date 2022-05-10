import weakref

class Context(object):
    """Stores application context"""
    _instances = weakref.WeakKeyDictionary()
    def _get(self):
        if hasattr(self, '_context'):
            return self._context
        self._context = Context._instances.setdefault(self.__class__, {})
        return self._context
    def _set(self, context):
        self._context = context
    context = property(_get, _set)

    def __init__(self, context=None):
        self.context = context or {}

    def __getitem__(self, key):
        return self.context[key]

    def __setitem__(self, key, value):
        self.context[key] = value

    def __contains__(self, key):
        return key in self.context

    def __str__(self):
        return str(self.context)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.context))
