import io
class File(io.RawIOBase):
	# Override these methods in a subclass:
    def read(self, size=-1):
        return self.file_obj.handle.read(size)
    def fileno(self):
        return self.file_obj.handle.fileno()
    def seekable(self):
        try:
            return super().seekable()
        except:
            return True
#	def readable(self):
#		return True
#	def writable(self):
#		return False
#	def seekable(self):
#		return True

	# Set this to an absolute the base URL for the site your server is
	# serving from. If not set, it'll default to the referrer in request
	# headers.
	_BASE_URL = None

	def __init__(self, filename, base=True):
		if base:
			self._BASE_URL = base
		if isinstance(filename, bytes):
			filename = filename.decode('utf-8')
		parts = werkzeug.urls.url_parse
