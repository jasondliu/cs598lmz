import weakref

from . import remote_api
from . import utils


class RemoteObject(remote_api.RemoteApi):
    """
    A remote object.

    It is the base of all objects that can be accessed remotely.
    """
    def __init__(self, remote_id, remote_class_name, api):
        super().__init__(api)
        self._remote_id = remote_id
        self._remote_class_name = remote_class_name
        self._api = api

    @property
    def remote_id(self):
        """
        The remote id of the remote object.
        """
        return self._remote_id

    @property
    def remote_class_name(self):
        """
        The remote class name of the remote object.
        """
        return self._remote_class_name

