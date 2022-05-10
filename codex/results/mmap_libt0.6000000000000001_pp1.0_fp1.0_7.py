import mmap
+
+def get_size(fileobj):
+    fileobj.seek(0,2) # move the cursor to the end of the file
+    size = fileobj.tell()
+    return size
+
+def read_in_chunks(file_object, chunk_size=1024*1024):
+    """Lazy function (generator) to read a file piece by piece.
+    Default chunk size: 1k."""
+    while True:
+        data = file_object.read(chunk_size)
+        if not data:
+            break
+        yield data
+
+
+def get_files(files, size):
+    for f in files:
+        if os.path.getsize(f) == size:
+            yield f
+
+
+def find_duplicates(files, size):
+    for f in files:
+        yield get_files(files, size)
+
+def main():
+    if len(sys.argv) < 2:
+        print "USAGE: duplicates.py
