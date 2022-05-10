import io
class File(io.RawIOBase):
	def read(self, size=-1):
		pass

	def readable(self):
		return True

	def writable(self):
		return False

	def seekable(self):
		return True

	def seek(self, pos, whence=0):
		pass

	def tell(self):
		pass

	def readinto(self, b):
		pass

class FileResolver(Resolver):
	"""
	Access files from http://github.com/raboof/wasm-research
	based on https://github.com/bytecodealliance/wasmtime-go/blob/master/wasm_go_api.go
	"""

	def __init__(self, directory):
		self.directory = directory

	def resolveFunc(self, params):
		fh = File(os.path.join(self.directory, params.filename.decode()))
		try:
			fh.seek(params.offset)
			return io.BytesIO(fh.read(params.size)).
