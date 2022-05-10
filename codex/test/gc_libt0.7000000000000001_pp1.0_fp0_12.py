import gc, weakref

class _Base(object):
    # A base object that implements an identity map,
    # which allows identity-based lookups.

    def __init__(self, id_):
        self.__id = id_
        self.__weakref = weakref.ref(self)

    id = property(lambda self: self.__id)

    @classmethod
    def by_id(cls, id_):
        return cls.__dict__['_' + cls.__name__ + '__weakref'](id_)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__id)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and \
               self.__id == other.__id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__class__, self.__id))

