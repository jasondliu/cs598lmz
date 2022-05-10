import weakref

class Object(object):
    def __init__(self, **attrs):
        self._attr_ = attrs
        self._attr_name_ = attrs.keys()
        self._attr_name_.sort()
        self._attr_name_ = tuple(self._attr_name_)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._attr_name_ == other._attr_name_ and \
                   all(self._attr_[n] == other._attr_[n]
                       for n in self._attr_name_)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        h = 0
        for name in self._attr_name_:
            h ^= hash(name)
            h ^= hash(self._attr_[name])
        return h

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,
                           ', '.join('
