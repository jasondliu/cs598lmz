import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from . import version
from . import watcher
from . import zkclient
from . import zktypes

log = logging.getLogger(__name__)


class ZKTransaction(object):
    """
    A transaction is a sequence of operations that are executed as a single
    atomic unit.

    The operations are executed in the order in which they are added to the
    transaction.

    If an operation fails, the transaction aborts, all previous operations are
    discarded, and none of the operations in the transaction are executed on
    the server.

    :param client: The client to use for the transaction.
    :type client: :class:`~kazoo.client.KazooClient`
    """
    def __init__(self, client):
        self.client = client
        self.ops = []

    def create(self, path, value=b"", acl=None, ephemeral=False,
               sequence=False, makepath=
