import selectors
import socket
import types

# 创建selectors对象
sel = selectors.DefaultSelector()


# 定义回显函数
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


# 定义读取函数
def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


# 创建socket对象
sock = socket.socket()
sock.bind(('localhost', 1234))
