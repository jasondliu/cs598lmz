import io
class File(io.RawIOBase):
	pass

class Blob(object):
	def __init__(self, name, content_type, data, parent_id=None, id=None):
		self.name = name
		self.content_type = content_type
		self.data = data
		self.parent_id = parent_id
		self.id = id
		self.size = len(data)
		self.content_hash = hashlib.md5(self.data).hexdigest()
		self.children = {}

	def get_child(self, name):
		return self.children[name]

	def get_children(self):
		return self.children.itervalues()

	def add_child(self, child):
		self.children[child.name] = child
		child.parent_id = self.id

	def delete_child(self, child):
		del self.children[child.name]

	def open_file(self):
		return File(self.data)

class BlobStore(
