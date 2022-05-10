from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')

def recv_msg(sock):
	raw_msglen = recvall(sock, 4)
	if not raw_msglen:
		return None
	msglen = s.unpack(raw_msglen)[0]
	return recvall(sock, msglen)


# send_msg
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')

def send_msg(sock, msg):
	msg = bytes(msg, encoding='utf-8')
	msglen = len(msg)
	sock.sendall(s.pack(msglen))
	sock.sendall(msg)

# recvall
def recvall(sock, n):
	data = b''
	while len(data) < n:
		packet = sock.recv(n - len(data))
		if not packet:
			return None
		data += packet
	return data

#
