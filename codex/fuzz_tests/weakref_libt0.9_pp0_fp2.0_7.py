import weakref

if sys.version_info.major < 3:
    from .Compat import is_bytes, bytes, unicode, str


def _pretty_str(self):
    """Returns a string describing self in detail."""
    if not hasattr(self, 'neighbor_list'):
        return self.__class__.__name__

    return '<{}#{} neighbors={}>'.format(
        self.__class__.__name__,
        self.state_id,
        self.neighbor_list.outgoing_state_ids)


class State(object):
    """Base class for all state types.

    The state object is really just a container for attributes
    like :attr:`!state_id`, :attr:`!label`, :attr:`!transitions`, etc.
    All state types inherit from it and these base classes, then add
    specific attributes in order to be useful.
    """

    __slots__ = ('state_id', 'label', 'transitions')
    __str__ = __unicode__ = _pretty_str


