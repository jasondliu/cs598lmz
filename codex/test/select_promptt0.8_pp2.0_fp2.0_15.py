import select
# Test select.select(inputs, outputs, error_sockets, timeout) with timeouts.
import socket
import time
from test.support import TESTFN, run_unittest, import_module
thread = import_module('thread')
tcp_ready = import_module('test.test_support').tcp_available
HOST = 'localhost'

def server(test, num_clients):

    def run_client(conn, id):
        conn.send(b'%5d' % id)
        response = conn.recv(1024)
        test.assertEqual(response, b'%5d' % id)
        conn.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, 0))
    sock.listen(128)
    clients = []
    for i in range(num_clients):
        conn, addr = sock.accept()
        t = thread.Thread(target=run_client, args=(conn, i))
        t.start()
        clients.append(t)
