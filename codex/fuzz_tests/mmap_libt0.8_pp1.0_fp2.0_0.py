import mmap
+import os
+import serial
+import socket
+import stat
+import struct
+import subprocess
+import sys
+import time
+import traceback
+
+if sys.version_info[0] == 2:
+    import Tkinter as tkinter
+    import tkFont
+else:
+    import tkinter
+    import tkinter.font as tkFont
+
+class Port(object):
+    def __init__(self, name=None, default=None, human=None,
+                 open_func=None, write_func=None, close_func=None):
+        self.name = name or 'port'
+        self.default = default or ''
+        self.human = human or name
+        self.open_func = open_func
+        self.write_func = write_func
+        self.close_func = close_func
+
+    def open(self):
+        if self.open_func:
+            return self.open_func()
+        else:
+            return
