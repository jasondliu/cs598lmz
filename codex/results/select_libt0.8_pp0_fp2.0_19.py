import select
+import signal
+import sys
+
+
+class TimeoutError(Exception):
+    pass
+
+
+class Timeout(object):
+    """
+    Timeout context manager
+    >>> with Timeout(1):
+    ...     print("This will get printed")
+    ...     with Timeout(2):
+    ...         print("This will not get printed")
+    ...         raise Exception("blah")
+    ...     print("This will get printed too")
+    ...     time.sleep(1.1)
+    ...     print("This will not get printed")
+    ...
+    ...
+    ...
+    ...
+    Traceback (most recent call last):
+      File "<stdin>", line 5, in <module>
+      File "<stdin>", line 2, in __exit__
+    __main__.TimeoutError: Timeout exception
+    """
+
+    def __init__(self, limit):
+        signal.signal(signal.SIGALRM, self.raise_timeout
