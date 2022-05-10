import _struct
+
+
+class CanFrame:
+
+    def __init__(self, line):
+        self.timestamp = float(line.split(' ', 1)[0])
+        self.frame_id = int(line.split('#', 1)[0].split(' ', 1)[1], 16)
+        self.frame_data = bytearray(
+            int(x, 16) for x in line.split(' ', 2)[2].split(' ')
+        ).tostring()
+
+        self.frame_type = (self.frame_id & 0x80000000) >> 31
+        self.frame_id = (self.frame_id & 0x7FFFFFFF)
+        self.frame_data_len = len(self.frame_data)
+
+    def __repr__(self):
+        return '<CanFrame(id={}, data={}, len={})>'.format(
+            hex(self.frame_id),
+            ''.join(hex(x) for x in self.frame_data),
+
