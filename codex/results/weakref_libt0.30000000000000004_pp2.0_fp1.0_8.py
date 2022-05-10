import weakref
import logging

from . import utils

logger = logging.getLogger(__name__)


class Base(object):
    """
    Base class for all objects.

    This class is the base for all objects in the :mod:`~pyglet.graphics`
    module.  It provides a common interface for all objects, and implements
    reference counting.

    :Ivariables:
        `id` : int
            Unique identifier for this object.
        `_refs` : list
            List of weak references to this object.
        `_deleted` : bool
            True if this object has been deleted.
    """

    _next_id = 0

    def __init__(self):
        self.id = Base._next_id
        Base._next_id += 1
        self._refs = []
        self._deleted = False

    def __del__(self):
        if not self._deleted:
            logger.warning('%r not deleted', self)

    def delete(self):
        """Delete this object.

        This method is called
