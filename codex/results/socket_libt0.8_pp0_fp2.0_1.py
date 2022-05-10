import socket
import sys

import domotica.logger as log


class TcpReceiver(object):
    """TCP connection receiver proxy class, will receive and handle incoming tcp connections.
    """

    def __init__(self, controller):
        """Initialize TCP receiver.

        :param domotica.Controller.Controller controller: Controller to be used.
        """
        self.controller = controller
        self.log = log.get_logger(self.controller.config, __name__)

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (self.controller.config.HOST, self.controller.config.PORT)
        self.log.debug("Starting up on %s port %s" % server_address)
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)

    def shutdown(self):
        """Shutdown TCP receiver.
        """
