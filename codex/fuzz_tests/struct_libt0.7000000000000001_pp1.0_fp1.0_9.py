import _struct

#define
BUFFSIZE = 8192

#function
def recvmsg(sock):
	msg = _struct.pack('I', 0)
	msg += sock.recv(BUFFSIZE)

	length = _struct.unpack('I', msg[:4])[0]
	return msg[4:length+4]


#function
def sendmsg(sock, msg):
	msg = _struct.pack('I', len(msg)) + msg
	sock.sendall(msg)


def recvall(sock):
	msg = ''
	while True:
		chunk = sock.recv(BUFFSIZE)
		if chunk == '':
			break
		msg += chunk
	return msg
