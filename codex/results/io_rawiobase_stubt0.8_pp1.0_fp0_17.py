import io
class File(io.RawIOBase):
	pass
class StringIO(io.StringIO):
	@property
	def name(self):
		return "StringIO"

class BytesIO(io.BytesIO):
	@property
	def name(self):
		return "BytesIO"

import os.path
class ResourceReader(object):
	path_sep='/'

	"""
	A class which can be used to read a resource by it's name path.
	
	This is a Python 3 version of the zope.app.file class.
	"""
	def __init__(self, module):
		"""
			ResourceReader constructor.

			The module argument is the module from which the resource will be read.
			An optional prefix argument can be supplied for all resources. This
			is a string which will be prepended to the path.
		"""
		if isinstance(module, type(sys)):
			module = module.__name__
		self._module = module
		self.resourcedict = {}

	def exportName(self
