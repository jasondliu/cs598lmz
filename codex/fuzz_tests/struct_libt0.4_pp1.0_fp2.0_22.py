import _struct
+
+#
+#
+#
+class Struct(object):
+    """
+    """
+
+    #
+    #
+    #
+    def __init__(self, format):
+        self.format = format
+        self.size = _struct.calcsize(format)
+
+    #
+    #
+    #
+    def pack(self, *args):
+        return _struct.pack(self.format, *args)
+
+    #
+    #
+    #
+    def unpack(self, data):
+        return _struct.unpack(self.format, data)
+
+    #
+    #
+    #
+    def unpack_from(self, data, offset=0):
+        return _struct.unpack_from(self.format, data, offset)

