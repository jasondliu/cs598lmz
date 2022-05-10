import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def writable(self):
        return False

    def readable(self):
        return True

    def readinto(self,b):
        print(b)
        return len(b)

f=File()
print(f.writeable())
print(f.readable())
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,fileno=f.fileno())
#s.connect(("127.0.0.1",9000))
#s.sendall(b"abc")
s.recv_into(b'11112222')
