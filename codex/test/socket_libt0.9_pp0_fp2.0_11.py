import socket
from threading import Thread

import time
import _thread

def main():
    clients = {} # dic of connection socket objects?
    ip_connections = {}
    clients_ids = []
    clients_ids_lock = _thread.allocate_lock()
    thread_connected = {"connected": False}
    thread_connected_lock = _thread.allocate_lock()

    port = 2424
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        #sys.exit()
    server_socket.listen(10)

