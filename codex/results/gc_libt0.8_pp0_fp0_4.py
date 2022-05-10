import gc, weakref, sys

_UNSET = object()

class _BuiltinMethod(object):
    def __init__(self, name):
        self.__name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        try:
            return getattr(obj._obj, self.__name)
        except AttributeError:
            raise NotImplementedError

class IDocRoot(Interface):
    pass

class DocElement(object):

    def __init__(self, doc, obj, name=None):
        self._doc = doc
        self._obj = obj
        self._name = name
        idocroot = IDocRoot(self._doc, _UNSET)
        if idocroot is not _UNSET:
            idocroot.docElements.append(self)

    def __repr__(self):
        return "%s(%r, %r, %r)" % (self.__class__.__name__,
                                   self._doc, self._obj, self._name)


