import gc, weakref
import threading

from boto.utils import get_instance_metadata
from boto.exception import NoAuthHandlerFound
from boto.connection import AWSAuthConnection
from scalarizr import config


class ScalarizrMessage:
    message_id = None
    timestamp = None
    from_hostname = None
    event_name = None
    event_object = None

    def __init__(self):
        self.timestamp = int(time.time())
        self.from_hostname = socket.gethostname()

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, str(self))

    def to_dict(self):
        return dict((attr, getattr(self, attr))
                     for attr in dir(self) if not attr.startswith('_'))

    @cached
    def _szr_version(self):
        from scalar
