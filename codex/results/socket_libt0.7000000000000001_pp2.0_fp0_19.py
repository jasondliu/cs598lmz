import socket
from threading import Thread
from threading import Lock
from threading import Condition

IP = "0.0.0.0"
PORT = 9999
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()

threads = []
lock = Lock()
cond = Condition(lock)
buffer_list = []


def handle_conn(conn, addr):
    print("Connection from {}".format(addr))
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        with cond:
            buffer_list.append(data)
            cond.notifyAll()
    conn.close()


def handle_data():
    while True:
        with cond:
            cond.wait_for(lambda: buffer_list)
            print(buffer_list.pop())


