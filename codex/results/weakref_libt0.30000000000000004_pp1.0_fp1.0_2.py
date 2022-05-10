import weakref

from . import util
from . import config
from . import log
from . import event
from . import client
from . import server
from . import protocol
from . import protocol_pb2
from . import protocol_pb2_grpc
from . import plugin
from . import plugin_pb2
from . import plugin_pb2_grpc
from . import error
from . import error_pb2
from . import error_pb2_grpc
from . import user
from . import user_pb2
from . import user_pb2_grpc
from . import client_pb2
from . import client_pb2_grpc
from . import server_pb2
from . import server_pb2_grpc
from . import event_pb2
from . import event_pb2_grpc

_logger = log.get_logger(__name__)


class _Service(protocol_pb2_grpc.ProtocolServicer):
    def __init__(self, server_instance):
        self._server_instance = server_instance

    def GetVersion(self, request,
