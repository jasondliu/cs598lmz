import io
class File(io.RawIOBase):
	def __init__(self, *args, **kwargs):
		super().__init__()
		#self.f = open(*args, **kwargs)
		self.f = io.StringIO()

	def read(self, size=-1):
		data = self.f.read(size)
		return data

	def write(self, b):
		return self.f.write(b)

	def fileno(self):
		return 0

	def close(self):
		self.f.close()

sys.stdout = File()
sys.stderr = File()

def init_logging(loglevel):
	"""
	Initialize logging to stdout, based on the requested log level.
	"""
	logging.basicConfig(
		stream=sys.stdout,
		format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
		level=loglevel,
		datefmt="%Y-%m-%
