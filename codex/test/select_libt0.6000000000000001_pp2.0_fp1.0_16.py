import selectors

from . import base
from . import util
from . import wsproto

logger = logging.getLogger(__name__)


class Connection(base.Connection):
    """Websocket connection."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ws = wsproto.Connection(wsproto.ConnectionType.CLIENT)
        self.ws.set_max_send_fragment_size(2 ** 16)
        self.ws.set_max_recv_message_size(2 ** 16)
        self.ws.set_max_recv_fragment_size(2 ** 16)
        self.sel = selectors.DefaultSelector()

    def _read(self, timeout=None):
        """Read a single message from the websocket connection.

        Returns None if the websocket was closed.
        """
        self.ws.send_ping()
        self.ws.recv_pong()

        events = self.sel.select
