import io
class File(io.RawIOBase):
	def __init__(self, socket):
		self.socket = socket
	def readable(self):
		return True
	def readinto(self, b):
		data = self.socket.recv(len(b))
		if not data:
			return None
		b[:len(data)] = data
		return len(data)
	def read(self, n=None):
		return self.socket.recv(n)
	def write(self, b):
		return self.socket.send(b)
	def writable(self):
		return True
	def fileno(self):
		return self.socket.fileno()
	def readline(self):
		return self.socket.recvline()
	def flush(self):
		return self.socket.flush()
	def close(self):
		return self.socket.close()

class Socket(basesocket.BaseSocket):
	def __init__(self, sock, sockfile = None):
		self.sock
