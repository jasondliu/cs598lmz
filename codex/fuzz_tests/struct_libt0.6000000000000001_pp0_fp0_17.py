import _struct

from . import util

class Message(object):
    """
    Base class for all messages
    """

    def __init__(self, header, payload):
        self.header = header
        self.payload = payload
        self.raw = self.header + self.payload

    def __len__(self):
        return len(self.raw)

    def __repr__(self):
        return repr(self.raw)

    def __str__(self):
        return str(self.raw)

    def __eq__(self, other):
        return self.raw == other

    def __hash__(self):
        return hash(self.raw)

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def from_raw(cls, data):
        """
        parses raw data into Message object
        """
        pass

    def to_raw(self):
        """
        serializes message into raw data
        """
        pass

class MessageHeader(object):
    """
