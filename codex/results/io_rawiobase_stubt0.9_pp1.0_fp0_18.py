import io
class File(io.RawIOBase):
	def __init__(self, file_name):
		self.f = open(file_name, "rb", buffering = 0)
	def raw_input(self, size: int) -> bytes:
		return self.f.read(size)
	def raw_output(self, b: bytes) -> None:
		self.f.write(b)
		self.f.flush()
	def raw_close(self) -> None:
		self.f.close()
	def raw_seek(self, pos: int, whence: io.SeekMode) -> int:
		return self.f.seek(pos, whence)
	def raw_tell(self) -> int:
		return self.f.tell()
	@classmethod
	def open(cls, name, mode=None, buffering = 0):
		return cls(name)
def uzlib_raw_read(f: io.File, size: int) -> bytes:
	return f.read(size)
def uzlib_raw_write(f:
