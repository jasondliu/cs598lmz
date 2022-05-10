import weakref
from xml.etree.cElementTree import iterparse


class Type(object):
    """
    The base class for all types.

    Types are used to describe the structure of data stored by a :class:`DataFrame`.

    Parameters
    ----------
    name : str, optional
        The name of the type.
    metadata : dict, optional
        Type-specific metadata that can be used to inform the encoding of the type.

    """
    __slots__ = 'name', 'metadata'

    def __init__(self, name=None, metadata=None):
        self.name = name
        self.metadata = metadata or {}

    def __repr__(self):
        return '%s()' % self.name

    def __eq__(self, other):
        return (type(self) is type(other)
                and self.name == other.name
                and self.metadata == other.metadata)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.name, self.metadata
