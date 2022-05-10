import selectors
import socket
import sys
import traceback

try:
    import simplejson as json
except ImportError:
    import json

# The client sends a 32-bit integer to the server indicating the number of
# integers that it will be sending. The server receives these integers and sums
# them. The server sends the sum back to the client. The client prints the
# response from the server.

# This is the same example as the echo server except that the client sends
# a message that is of a different size than what it receives.

SIZE = 10

host = sys.argv[1]
port = int(sys.argv[2])

messages = [(json.dumps({'input': i}), None) for i in range(SIZE)]
response_queue = queue.Queue()

sel = selectors.DefaultSelector()


def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
