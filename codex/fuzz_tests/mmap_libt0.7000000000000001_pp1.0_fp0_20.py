import mmap
+from cStringIO import StringIO
+from collections import defaultdict, namedtuple
+
+from . import _xml
+from . import _table
+from . import _record
+from . import _field
+from . import _relationship
+from . import _memo
+from . import _exception
+from . import _constants
+
+
+class File(_xml.XMLRecordMixin):
+    """Representation of a Firebird database file."""
+    _format = '<2s2x2H3x8xL2x'
+    _field_format = '<H'
+
+    def __init__(self, filename):
+        self._filename = filename
+        self._fd = open(filename, 'rb')
+        self._fd.seek(20)
+        self._xml_record_offset = unpack(self._format, self._fd.read(28))[-1]
+        self._memos = _memo.MemoFile(filename)
+        self._relationships = []
+        self
