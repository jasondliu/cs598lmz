import io
class File(io.RawIOBase):
	def __init__(self, path, mode):
		super().__init__()
		self._path = path
		self._mode = mode
		self._f = None
	def readinto(self, b):
		return self._f.readinto(b)
	def write(self, b):
		return self._f.write(b)
	def __enter__(self):
		self._f = open(self._path, self._mode)
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self._f.close()


def main():
	f = File('/tmp/file.txt', 'w')
	with f:
		f.write(b'Hello')
		f.seek(0)
		print(f.read())

if __name__ == '__main__':
	main()
