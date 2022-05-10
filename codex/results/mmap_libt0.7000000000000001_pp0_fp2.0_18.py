import mmap
+
+
+def read_file(file_path):
+    """
+    Read csv file with mmap and return list of lines
+    :param file_path: Path to the file
+    :return: List of lines
+    """
+    result = []
+    with open(file_path, "r+b") as file:
+        mmapped = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
+        for line in iter(mmapped.readline, b""):
+            result.append(line.decode('utf-8'))
+
+    return result
+
+
+def write_file(file_path, lines):
+    """
+    Writes lines to csv file
+    :param file_path: Path to the file
+    :param lines: Lines to write to the file
+    :return: None
+    """
+    with open(file_path, 'w') as csv_file:
+        csv_writer = csv.writer(csv
