import weakref

from . import utils
from . import exceptions
from . import constants


class Base(object):
    """
    Base class for all objects in the library.
    """

    def __init__(self, client, **kwargs):
        self._client = client
        self._update(kwargs)

    def _update(self, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<{0} {1}>'.format(self.__class__.__name__, self.id)


class User(Base):
    """
    A user object.
    """

    def __init__(self, client, **kwargs):
        super(User, self).__init__(client, **kwargs)
        self._update(kwargs)

    def get_playlists(self):
        """
        Get all playlists created by this user.
        """
        return [
            Playlist(self._client, **playlist)
            for
