import socket
import sys
import threading
import traceback

if sys.platform == 'win32':
    from win32clipboard import *
    from win32con import *

log = logging.getLogger('em_clipboard_server')


class clipboard_server:

    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.sock.bind(('0.0.0.0', port))
        except:
            print('Error binding to port. Another instance is already running ?')
            sys.exit(2)

    def server_loop(self):
        log.info('Starting on port %i' % self.port)
