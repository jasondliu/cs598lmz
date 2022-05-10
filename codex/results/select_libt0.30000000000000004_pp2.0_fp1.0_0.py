import select
import socket
import sys
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

__all__ = ['Client']

LOGGER = logging.getLogger(__name__)


class Client(object):
    """A client for the MQTT v3.1.1 protocol.

    This class implements the client side of the MQTT v3.1.1 protocol.
    See http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html
    for the protocol specification.

    This is a low level client class. Most applications will want to use
    :class:`~paho.mqtt.client.Client` instead.

    """
    def __init__(self, client_id="", clean_session=True, userdata=None,
                 protocol=constants.MQTTv311, transport="tcp"):
        """Create a new client instance.

        :param client_id
