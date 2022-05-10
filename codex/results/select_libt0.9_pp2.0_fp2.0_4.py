import select
import socket
import time

# local imports
import logger
import util

log = logger.getLogger('listener')

class Listener(object):
    """
    A read listener. The specified socket is read and the results pushed to the
    callback. If the remote/local disconnects, a callback is provided to
    appropriately handle that.
    """

    def __init__(self, sock, callbacks, select_timeout=.01):
        self.sock = sock
        self.callbacks = callbacks
        self.select_timeout = select_timeout

    def start(self):
        """
        Start the listener. Blocks.
        """
        keep_running = True
        readable = []

        while keep_running:
            for s in readable:
                try:
                    data = util.sock_read(s, self.callbacks['set_disconnect'])
                    if not data:
                        continue
                    self.callbacks['set_data'](data)
                except socket.error, e:
                    log.debug("Error reading from socket: %s", e
