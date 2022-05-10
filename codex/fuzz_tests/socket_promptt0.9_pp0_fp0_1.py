import socket
# Test socket.if_indextoname
socket.if_indextoname(100)
# Test SocketServer.ThreadingMixin.make_request
SocketServer.ThreadingMixin().make_request(None, None, None)
# Test socket.socket
socket.socket()
# Test socket.socket.connect
socket.socket().connect((None, None))
# Test socket.socket.listen
socket.socket().listen(1)
# Test socket.socket.setsockopt
socket.socket().setsockopt(1, 1, 1)
# Test socket.socket.send
socket.socket().send(0,0,0)
# Test socket.socket.setsockopt_string
socket.socket().setsockopt_string(0, "val")
# Test socket.socket.ioctl.TIOCGPTN
socket.socket().ioctl(int(2147483675), 0, 0)
# Test socket.socket.ioctl.TIOCSPTLCK
socket.socket().ioctl(int(2147483670), 0, 0)
# Test socket.socket.ioctl.SIOCADDRT

