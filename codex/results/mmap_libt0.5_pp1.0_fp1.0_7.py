import mmap
+import os
+import signal
+import socket
+import sys
+import threading
+import time
+
+import numpy as np
+
+from pylibfreenect2 import FrameType, Registration, Frame, FrameMap, SyncMultiFrameListener, CpuPacketPipeline
+
+from pylibfreenect2 import createConsoleLogger, setGlobalLogger
+from pylibfreenect2 import LoggerLevel
+
+
+try:
+    from pylibfreenect2 import OpenGLPacketPipeline
+    pipeline = OpenGLPacketPipeline()
+except:
+    try:
+        from pylibfreenect2 import OpenCLPacketPipeline
+        pipeline = OpenCLPacketPipeline()
+    except:
+        from pylibfreenect2 import CpuPacketPipeline
+        pipeline = CpuPacketPipeline()
+print("Packet pipeline:", type(pipeline).__name__)
+
+# Create and set logger
+logger = create
