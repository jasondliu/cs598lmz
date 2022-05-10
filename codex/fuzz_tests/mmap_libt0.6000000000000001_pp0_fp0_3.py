import mmap
+import datetime
+import sys
+import os
+import csv
+
+
+
+
+def WriteToCSV(file_name, data_dict):
+    with open(file_name, 'a', newline='') as csvfile:
+        fieldnames = ['time','unixtime','x','y','z']
+        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
+        writer.writerow(data_dict)
+
+
+def ConvertToCSV(file_name):
+    with open(file_name, 'r') as f:
+        file_size = os.path.getsize(file_name)
+        mm = mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_READ)
+
+    while True:
+        line = mm.readline()
+        if not line:
+            break
+
+        line = line.decode("utf-8")
+        data_dict = {}
+        data_
