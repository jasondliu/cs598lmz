import io
class File(io.RawIOBase):
	def __init__(self, f):
		self.f = f
	def read(self, n):
		return self.f.read(n)

class Socket(io.RawIOBase):
	def __init__(self, sock):
		self.sock = sock
	def readinto(self, b):
		return self.sock.recv_into(b)

class SocketServer(io.RawIOBase):
	def __init__(self, sock):
		self.sock = sock
	def readinto(self, b):
		(s, addr) = self.sock.accept()
		return s.recv_into(b)

class Process(io.RawIOBase):
	def __init__(self, proc):
		self.proc = proc
	def readinto(self, b):
		return self.proc.stdout.readinto(b)

import subprocess
class Subprocess(io.RawIOBase):
	def __init__(self, cmd):
		self.
