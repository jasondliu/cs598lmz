import mmap
+
+
+class Kmreader(object):
+    """
+    Reads a binary knx/ip monitor file.
+    """
+
+    def __init__(self, filename, mode="rb"):
+        self.filename = filename
+        self.mode = mode
+        self.f = open(filename, mode)
+        self.mm = mmap.mmap(self.f.fileno(), 0, prot=mmap.PROT_READ)
+
+    @property
+    def header(self):
+        header = collections.OrderedDict()
+        header["magic"] = self.mm[:2]
+        header["version"] = self.mm[2:6]
+        header["caps"] = self.mm[6:]
+        return header
+
+    def check_magic(self):
+        if self.header["magic"] != "KM":
+            raise ValueError("Wrong file format, expected 'KM'")
+
+
+if __name__ == "__main__":
+
