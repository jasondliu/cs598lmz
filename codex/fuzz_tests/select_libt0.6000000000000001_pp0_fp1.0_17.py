import selectors
import sys
from time import time


from server_config import NODES, BUFSIZ, MAX_CHECK_PERIOD, MAX_CLIENTS
sel = selectors.DefaultSelector()

def create_request(action, value):
    if action == 'fib':
        n = int(value)
        if n > 0:
            return '{}:fib:{}'.format(n, value)
    elif action == 'factor':
        n = int(value)
        if n > 0:
            return '{}:factor:{}'.format(n, value)
    else:
        return 'unknown action: {}'.format(action)

def start_connection(host, port, request):
    addr = (host, port)
    print('starting connection to', addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = lib
