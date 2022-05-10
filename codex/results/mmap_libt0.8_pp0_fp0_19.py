import mmap
+import contextlib
+import os
+
+def read_data(path):
+    """
+    Returns the content of a file in a string
+
+    :param path:
+    :return:
+    """
+    _,ext = os.path.splitext(path)
+    if ext == ".gz":
+        f = gzip.open(path,'rt')
+    else:
+        f = open(path, 'rt',encoding='utf-8')
+    with f:
+        return f.read()
+
+def split_file(path,count):
+    """
+    Split a file into n_files parts
+
+    :param path:
+    :param count:
+    :return:
+    """
+    partfilename = re.compile(os.path.splitext(path)[0] + "_(\d+)" + os.path.splitext(path)[1])
+    paths = []
+
+    for filename in os.listdir('.'):
+        m =
