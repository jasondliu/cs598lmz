import _struct
+
+import sys
+import os
+
+
+def main():
+    # Read the file
+    with open(sys.argv[1], 'rb') as f:
+        data = f.read()
+
+    # Get the length of the data, and unpack it into an integer
+    data_len = len(data)
+    data_len, = _struct.unpack('I', data[:4])
+
+    # Make sure we agree on the length of the data
+    if data_len != data_len:
+        raise RuntimeError("Data length mismatch!")
+
+    # Get all the file records
+    file_recs_raw = data[4:]
+    file_recs = []
+    while len(file_recs_raw) > 0:
+        # Get and check the length of this record, then unpack
+        rec_len, = _struct.unpack('I', file_recs_raw[:4])
+        if len(file_recs_raw) < rec_len
