import _struct

from . import constants
from . import exceptions
from . import util
from . import watch
from . import znode


class ZooKeeper(object):
    """
    ZooKeeper connection.
    """

    def __init__(self, hosts, timeout=10000, watch_callback=None,
                 allow_unencrypted=False):
        """
        Connect to a ZooKeeper cluster.

        :param hosts: ZooKeeper server host:port pairs, separated by commas.
        :type hosts: string

        :param timeout: Session timeout in milliseconds.
        :type timeout: int

        :param watch_callback: Function to call with watch events.
        :type watch_callback: callable

        :param allow_unencrypted: Allow unencrypted connections.
        :type allow_unencrypted: bool

        :raises kazoo.exceptions.KazooException:
        """
        self.timeout = timeout
        self.hosts = hosts
        self.client_id = None
        self.session_id = None
        self.session_passwd = None
