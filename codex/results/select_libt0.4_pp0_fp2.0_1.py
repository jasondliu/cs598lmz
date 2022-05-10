import select
import sys
import time

from . import _common
from . import _compat
from . import _connection
from . import _exceptions
from . import _message
from . import _pool
from . import _utils
from . import constants
from . import exceptions
from . import protocol


__all__ = ['BlockingConnection', 'BlockingChannel']


_logger = logging.getLogger(__name__)


class BlockingChannel(_common.AMQPChannel):
    """
    This is a blocking version of :class:`pika.channel.Channel`.
    """
    def __init__(self, connection, channel_number):
        """
        Create a new instance of the BlockingChannel

        :param pika.connection.Connection connection: The connection
        :param int channel_number: The channel number for this instance
        """
        super(BlockingChannel, self).__init__(connection, channel_number)
        self._connection = connection
        self._channel_number = channel_number
        self._is_open = False
        self._consumer_infos = {}
