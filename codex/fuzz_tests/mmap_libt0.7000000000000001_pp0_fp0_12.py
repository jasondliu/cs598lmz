import mmap
+
+
+def slice_file(filename, size=1024*1024*50):
+    """
+    Slices a file into smaller files of the specified size
+
+    Parameters
+    ----------
+    filename: str
+        The file to be sliced
+    size: int
+        The target size of each subfile.
+
+    Returns
+    -------
+
+    """
+    with open(filename, "rb") as f:
+        file_size = os.fstat(f.fileno()).st_size
+        current_size = 0
+        buffer = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        buffer_size = buffer.size()
+        n_files = int(math.ceil(file_size/size))
+        for i in range(n_files):
+            if current_size < buffer_size:
+                name = filename.split(".")[0] + "_" + str(i) + "." + filename.split(".")[
