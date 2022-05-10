import _struct

from . import exceptions
from . import message
from . import objects


class TLSCB:
    def __init__(self, tls_info=None, tls_config=None):
        self.tls_config = tls_config
        self.tls_info = tls_info
        self.logger = logging.getLogger(__name__)

    def connection_made(self, sock):
        pass

    def connection_lost(self, exc):
        self.logger.debug("Closing TLS connection: %s", exc)

    def user_authenticate_cb(self, conn, username, password):
        self.logger.debug("User authentication called but not implemented")
        return False

    def user_auth_serv_cb(self, conn, username, cookie, method):
        self.logger.debug("User auth server called but not implemented")
        return []

    def socket_readable_cb(self, sock):
        data = sock.recv(4096)
        if not data:
            sock.close()
            return False

