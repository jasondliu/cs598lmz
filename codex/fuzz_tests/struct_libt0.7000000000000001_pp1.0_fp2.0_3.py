import _struct
+
+from . import utils
+from . import constants
+
+class _Base(object):
+    _header_fmt = '<4s3i'
+    _header_size = struct.calcsize(_header_fmt)
+    _header_unpack = struct.Struct(_header_fmt).unpack_from
+
+    def __init__(self, fileobj):
+        self.header = utils.Header(fileobj, self._header_unpack, self._header_size)
+        self.body = self.fetch(fileobj)
+
+    def __getitem__(self, key):
+        return self.body[key]
+
+    def __repr__(self):
+        return '<{}>'.format(self.__class__.__name__)
+
+    def fetch(self, fileobj):
+        raise NotImplementedError
+
+class _Symbol(_Base):
+    _fmt = '<8s7i'
+    _size = struct.
