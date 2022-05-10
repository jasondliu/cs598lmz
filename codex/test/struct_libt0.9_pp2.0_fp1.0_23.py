import _struct

class Struct:

    def __init__(self, **kwargs):
        self.members().update(kwargs)

    def members(self):
        try:
            return self.__dict__['__members__']
        except KeyError:
            self.__members__ = {}
            return self.__members__

    def __len__(self):
        return len(self.members())

    def __iter__(self):
        return iter(self.members().items())

    def __getitem__(self, key):
        return self.members()[key]

    def __setitem__(self, key, value):
        self.members()[key] = value

    def __contains__(self, key):
        return key in self.members()

    def __delitem__(self, key):
        del self.members()[key]

    def __repr__(self):
        pairs = []
        for key, value in self:
            pairs.append('%s=%r' % (key, value))
