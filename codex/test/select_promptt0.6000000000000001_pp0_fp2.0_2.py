import select
# Test select.select

import socket
import select
import threading

class TestSelect(object):
    
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('0.0.0.0', 12345))
        self._socket.listen(5)
        
        self._thread = threading.Thread(target=self._thread_func)
        self._thread.start()
        
