import socket
import sys
from threading import (
    Thread,
    current_thread,
    )
from time import (
    sleep,
    time,
    )
from uuid import (
    uuid4,
    )

from zmq import (
    EAGAIN,
    POLLIN,
    PUB,
    PULL,
    SUBSCRIBE,
    ZMQError,
    )
import zmq.green as zmq

from kazoo.recipe.election import Election

from pytools.retry import retry
from pytools.log import (
    StreamLogger,
    )


class BasePublisher(Thread):

    def __init__(self, topic_prefix, machine_id,
            poll_interval=10, log_level=logging.INFO):
        super(BasePublisher, self).__init__()
        self.daemon = True

        self.topic_prefix = topic_prefix
        self.machine_id = machine_id
        self.poll_interval = poll_interval
