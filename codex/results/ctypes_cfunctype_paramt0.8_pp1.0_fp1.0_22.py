import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Callback(object):
	def __init__(self, f):
		self.f = f
		self.functype = FUNTYPE(self.invoke)
		self.func = self.functype(self)

	def __call__(self, *args, **kwargs):
		raise Exception("Cannot call this class directly, invoke through func instead")

	def invoke(self, *args, **kwargs):
		self.f(*args, **kwargs)

class PyScsiBase(object):
	def close(self):
		del self.device
		self.device = None

	def open(self):
		self.device.open()

	def __enter__(self):
		self.device.open()
		return self

	def __exit__(self, type, value, traceback):
		self.device.close()

class PyScsiInquiry(PyScsiBase):
	def __init__(self, device, id=0, timeout=5):
		self
