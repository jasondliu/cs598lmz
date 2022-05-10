import _struct
# Test _struct.Struct
_struct.Struct(">i").pack(100)
# Test _struct.pack
_struct.pack(">i", 100)
# Test _struct.unpack
_struct.unpack(">i", _struct.pack(">i", 100))[0]

# Test _socket
import _socket
# Test _socket.socket
_socket.socket(_socket.AF_INET, _socket.SOCK_STREAM).connect(("127.0.0.1", 80))
# Test _socket.socketpair
(_socket.socket(_socket.AF_INET, _socket.SOCK_STREAM),
 _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM))
# Test _socket.gethostbyname
_socket.gethostbyname("www.google.com")
# Test _socket.gethostname
_socket.gethostname()
# Test _socket.getprotobyname
_socket.getprotobyname("tcp")
# Test _socket.getservbyname
_socket.getservbyname("ssh")
# Test
