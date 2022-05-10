import mmap
+import os
+import sys
+import time
+
+
+class Logger:
+    def __init__(self, filename, level=logging.INFO):
+        self.logger = logging.getLogger(__name__)
+        self.logger.setLevel(level)
+        formatter = logging.Formatter(
+            "%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
+        )
+        fh = logging.FileHandler(filename)
+        fh.setLevel(level)
+        fh.setFormatter(formatter)
+        self.logger.addHandler(fh)
+
+    def log(self, message, level=logging.INFO):
+        if level == logging.INFO:
+            self.logger.info(message)
+        elif level == logging.ERROR:
+            self.logger.error(message)
+        elif level == logging.DEBUG:
+            self.
