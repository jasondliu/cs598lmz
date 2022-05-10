import weakref

from . import _compat
from . import _util


class _Base(object):
    """Base class for all objects in the API.

    This class provides the ability to set and get arbitrary properties on
    objects. It also provides a simple way to print a human-readable
    representation of an object.
    """

    def __init__(self, properties=None, client=None):
        """Constructor.

        Args:
            properties (dict): Initial properties values. It is treated as a
                snapshot of the resource state.
            client (:class:`~google.cloud.bigquery.client.Client`):
                A client which holds credentials and project configuration
                for the dataset (which requires a project).
        """
        self._properties = properties or {}
        self._client = client

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return other._properties == self._properties

    def __ne__(self, other):
        return not self == other

