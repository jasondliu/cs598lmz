import _struct

#
#
#
class UUID:
    def __init__(self, uuid):
        self.uuid = uuid

    def __str__(self):
        return self.uuid

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, UUID):
            return self.uuid == other.uuid
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.uuid)

    def __cmp__(self, other):
        if isinstance(other, UUID):
            return cmp(self.uuid, other.uuid)
        else:
            return -1

    def __getitem__(self, index):
        return self.uuid[index]

    def __len__(self):
        return len(self.uuid)

#
#
#
