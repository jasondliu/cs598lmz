import mmap
+import os
+import sys
+import tempfile
+
+
+def main(argv):
+    parser = argparse.ArgumentParser()
+    parser.add_argument('--offset', type=int, default=0)
+    parser.add_argument('--length', type=int, default=0)
+    parser.add_argument('--host', type=str)
+    parser.add_argument('--port', type=int)
+    parser.add_argument('--file', type=str)
+    parser.add_argument('--mmap', action='store_true')
+    parser.add_argument('--verbose', action='store_true')
+    parser.add_argument('--log', type=str)
+    args = parser.parse_args(argv)
+
+    if args.verbose:
+        logger = log.getLogger()
+        logger.setLevel(log.DEBUG)
+        logger.addHandler(log.StreamHandler())
+        if args.log:
+            logger.addHandler
