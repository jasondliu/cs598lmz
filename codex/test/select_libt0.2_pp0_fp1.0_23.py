import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import constants
from . import errors
from . import utils
from . import wire
from . import wire_format
from . import wire_format_pb2
from . import wire_format_pb2_grpc
from . import wire_pb2
from . import wire_pb2_grpc
from . import wire_types
from . import wire_util
from . import wire_util_pb2
from . import wire_util_pb2_grpc

_LOGGER = logging.getLogger(__name__)


class _RpcState(object):
    """State for an RPC.

    This class is not thread-safe.
    """

    def __init__(self, request_id, method, timeout, metadata, credentials):
        self.request_id = request_id
        self.method = method
        self.timeout = timeout
        self.metadata = metadata
        self.credentials = credentials
        self.code = None
