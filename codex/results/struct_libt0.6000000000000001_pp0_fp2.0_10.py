import _struct
import _time
import _thread
import _socket

# Based on CPython's socket.py
try:
    import _ssl
except ImportError:
    _ssl = None

if sys.platform == 'win32':
    import _winapi
    import msvcrt
    import _overlapped

def sock_call(func, *args):
    while True:
        try:
            return func(*args)
        except InterruptedError:
            pass

def sock_recv(sock, length, flags=0):
    return sock_call(sock.recv, length, flags)

def sock_recv_into(sock, buffer, nbytes=None, flags=0):
    return sock_call(sock.recv_into, buffer, nbytes, flags)

def sock_sendall(sock, data, flags=0):
    return sock_call(sock.sendall, data, flags)

def sock_connect(sock, address):
    return sock_call(sock.connect, address)

def sock
