import weakref

from . import _impl
from . import _internal
from . import _types

__all__ = ['Entity', 'EntityDictionary', 'Service', 'ServiceDictionary']


class Entity:
    """
    Represents a single entity in the database.

    Attributes
    ----------
    name : str
        The name of the entity.
    definitions : dict of str -> dict
        The definitions of the entity. The keys are the names of the
        definitions, and the values are the definition dictionaries.
    """

    def __init__(self, name, definitions):
        self.name = name
        self.definitions = definitions

    def __str__(self):
        return '<Entity %s>' % self.name

    def __repr__(self):
        return '<Entity %s>' % self.name

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Entity):
            return False
        return self.name == other.name

