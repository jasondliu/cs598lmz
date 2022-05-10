import weakref

class Object(object):
    def __init__(self, _id, _type=None):
        self._id = _id
        self._type = _type
        self.__weakref__ = weakref.ref(self)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__,
                           self._id)

    def __eq__(self, other):
        if isinstance(other, Object):
            return self._id == other._id
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, Object):
            return self._id != other._id
        return NotImplemented

    def __hash__(self):
        return hash(self._id)


class User(Object):
    def __init__(self, _id, _type=None, name=None, screen_name=None, description=None,
                 statuses_count=None, friends_count=None, followers_count=None,
                 listed_count=
