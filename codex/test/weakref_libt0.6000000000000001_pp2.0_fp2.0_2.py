import weakref

from .. import logging_helper
from ..util import datatypes


class Remote(datatypes.Enum):
    """
    This is an enum that describes the remote used to request the data
    """
    UNKNOWN = -1
    """
    Unknown remote
    """
    LOCAL = 0
    """
    Local remote, this is the default remote
    """
    REMOTE = 1
    """
    Remote remote
    """


class DataSource(object):
    """
    This is a base class for all data sources
    """

    def __init__(self, data_source_id):
        """
        Initialises the data source

        :param data_source_id: The data source id
        :type data_source_id: str
        """
        # Setup the logger
        self._logger = logging_helper.Logger(__name__)

        # The data source id
