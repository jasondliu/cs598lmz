import _struct
import sys

def hb_struct(code, msg):
    return _struct.pack('!i' + str(len(msg)) + 's', code, msg)

def hb_unpack(data):
    s = _struct.Struct('!i')
    return s.unpack(data[:4])[0]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8888))
sock.send(hb_struct(1, 'Hello'))
print(hb_unpack(sock.recv(1024))) # Just for dumb purpouse. We can simply do sock.recv(size). But leaving it like this to show off 
</code>
Server
<code>import socket
import _struct

def hb_struct(code, msg):
    return _struct.pack('!i' + str(len(msg)) + 's', code, msg)

def hb_unpack(data):
    s = _struct.Struct('!i')
