import weakref

from . import _core
from . import _util
from . import _py2to3

from . import _core
from . import _util
from . import _py2to3

class _Data(object):
    """
    A data object that can be used to store arbitrary data in a
    :class:`~matplotlib.artist.Artist`.

    """
    def __init__(self, **kwargs):
        self.update(kwargs)

    def update(self, kwargs):
        """
        Update the data dictionary with the values in *kwargs*.

        """
        self.__dict__.update(kwargs)

    def __str__(self):
        return "{" + ", ".join(["%s: %s" % (k, v) for k, v in self.__dict__.items()]) + "}"


class Artist(object):
    """
    Abstract base class for someone who renders into a
    :class:`~matplotlib.backend_bases.Renderer`.

    The following methods are provided for interaction with
