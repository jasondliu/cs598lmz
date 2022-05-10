import _struct

hostname = '202.112.51.248'
port = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))

# 在第一个长度字段之前填充三个字节
# 在第一个长度字段之后填充23个字节
buf = 'A' + 23*'B' + _struct.pack('!i', len(buf)) + 'C'

s.send(buf)
print s.recv(1024)
s.close()
