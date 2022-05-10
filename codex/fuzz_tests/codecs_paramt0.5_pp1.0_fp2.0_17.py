import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _py2to3
from . import _json as json
from . import _util
from . import _compat
from . import _logging
from . import _config
from . import _errors
from . import _schemas


_log = _logging.getLogger(__name__)
_log.addHandler(_logging.NullHandler())


class Config(object):
    """
    Configuration object.

    This object is used to load, access and save the configuration data.

    :param path: The path to the configuration file.
    :type path: str
    """

    def __init__(self, path=None):
        """
        Create a new configuration object.
        """
        self._path = path
        self._data = {}

    @property
    def path(self):
        """
        The path to the configuration file.

        :type: str
        """
        return self._path

    @property
    def data(self):
        """
        The loaded configuration data.

        :
