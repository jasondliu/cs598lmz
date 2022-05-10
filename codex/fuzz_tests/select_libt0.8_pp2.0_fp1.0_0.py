import selectors
import socket


# def accept(sock, mask):
#     conn, addr = sock.accept()  # Should be ready
#     print('accepted', conn, 'from', addr)
#     conn.setblocking(False)
#     sel.register(conn, selectors.EVENT_READ, read)
#
#
# def read(conn, mask):
#     data = conn.recv(1000)  # Should be ready
#     if data:
#         print('echoing', repr(data), 'to', conn)
#         conn.send(data)  # Hope it won't block
#     else:
#         print('closing', conn)
#         sel.unregister(conn)
#         conn.close()
#
#
# sel = selectors.DefaultSelector()
#
# lsock = socket.socket()
# lsock.bind(('localhost', 1234))
# lsock.listen()
# print('listening on', ('localhost', 1234))
# lsock.setblocking(False)
# sel.
