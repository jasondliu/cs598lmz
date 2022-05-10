import selectors
import socket
import types

# 服务器地址
HOST = '0.0.0.0'
PORT = 65432

sel = selectors.DefaultSelector()

# 封装一个 Request 对象
class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []
    def add_done_callback(self, fn):
        self._callbacks.append(fn)
    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)
# Selector 对象的回调函数
def accept(sock, mask):
    conn, addr = sock.accept()
    conn.setblocking('True')
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)
    if data:
        future.set_result(
