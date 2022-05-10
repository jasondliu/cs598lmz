import mmap
+import threading
+import time
+
+SIZE_OF_LONG = 4
+
+class DeviceSemaphore(object):
+
+    def __init__(self, name):
+        self._filename = "/tmp/" + name
+        self._lock = threading.Lock()
+        self._resetSemaphore()
+        self._map = self._createMmap()
+
+    def _resetSemaphore(self):
+        self._fd = open(self._filename, "wb")
+        self._fd.seek(SIZE_OF_LONG - 1)
+        self._fd.write(b"\x00")
+        self._fd.close()
+
+    def _createMmap(self):
+        self._fd = open(self._filename, "r+b")
+        return mmap.mmap(self._fd.fileno(), SIZE_OF_LONG)
+
+    def lock(self):
+        """
+        Will block until it can acquire the lock
+        """
+        while
