import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def start_socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 0))
    s.listen(1)
    _, port = s.getsockname()
    t = threading.Thread(target=socket_server, args=(s,))
    t.daemon = True
    t.start()
    return port

def socket_server(s):
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=socket_conn, args=(conn,))
        t.daemon = True
        t.start()

def socket_conn(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)

def get_dll_filename():
    if sys.platform == "win32":
        dll_name
