import weakref

class URL(object):
	"""
	Class representing a single URL download.
	"""
	downloading = False
	def __init__(self, url, filename, context = None, progress = None, userdata = None):
		self.url = url
		self.filename = filename
		self.progress = progress
		self.context = context
		self.userdata = userdata

	def download(self):
		"""
		Starts the download.
		"""
		encoded = self.url.encode('ascii')
		if encoded.startswith('http://'):
			if self.context:
				self.downloading = True
				self.task = _LibWebDownloadTask(self)
				self.task.start(self.url, self.filename, self.context, self.progress, self.userdata)
			else:
				raise RuntimeError('HTTP download requested, but no context specified')
		else:
			raise ValueError
