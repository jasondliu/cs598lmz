import mmap
+from io import BytesIO
+from io import SEEK_SET, SEEK_CUR, SEEK_END
+
+from PIL import Image
+
+from mmapy import MMAPy, read_int_from_file
+
+MAGIC_MMB = 0x424d4d
+
+
+class MMBDecoder(object):
+    def __init__(self, path):
+        self.mmap = MMAPy(path, 0, mmap.MAP_PRIVATE, mmap.PROT_READ).map
+        self.filepos = self.filepos_next = 0
+
+    def _init(self):
+        self.filepos = self.filepos_next = 0
+
+    def unpack_int(self, n=4):
+        buf = self.mmap[self.filepos:self.filepos + n]
+        self.filepos_next = self.filepos + n
+        return read_int_from_file(BytesIO(buf))
+
+    def unpack
