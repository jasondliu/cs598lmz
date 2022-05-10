import weakref

from . import exceptions
from . import helpers


class BaseObject(object):
    """
    Base object for all objects in the library.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the object.
        """
        self._client = kwargs.pop('client', None)
        self._client_ref = None

        if self._client:
            self._client_ref = weakref.ref(self._client)

    @property
    def client(self):
        """
        Return the client.
        """
        return self._client_ref()


class BaseResource(BaseObject):
    """
    Base resource for all resources in the library.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the resource.
        """
        super(BaseResource, self).__init__(*args, **kwargs)

        self._attributes = {}
        self._changed = set()
        self._exists = False

    @property
    def attributes(self):
