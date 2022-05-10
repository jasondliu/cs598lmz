import io
class File(io.RawIOBase):
	def __init__(self, fp):
		self.fp = fp

	def read(self, count=-1):
		return self.fp.read(count)

	def write(self, data):
		return self.fp.write(data)

def auto_close(obj, method_name, close_method_name="close"):
	old_method = getattr(obj, method_name)
	def new_method(*args, **kwargs):
		try:
			return old_method(*args, **kwargs)
		except:
			if getattr(obj, close_method_name) is not None:
				obj.close()
			raise
	setattr(obj, method_name, new_method)

def auto_close_read(obj):
	auto_close(obj, "read")

def auto_close_write(obj):
	auto_close(obj, "write")

class AutoCloseRawIOBase(io.RawIOBase):
	def __init__(self
