import select
+import datetime
+import time
+import sys
+import argparse
+
+
+def main():
+    parser = argparse.ArgumentParser(
+        description='Runs a command until it succeeds',
+        formatter_class=argparse.ArgumentDefaultsHelpFormatter
+    )
+    parser.add_argument('--interval', '-i', default=1, type=int,
+                        help='Interval between command runs, in seconds')
+    parser.add_argument('--timeout', '-t', default=0, type=int,
+                        help='Timeout, in seconds. 0 means no timeout.')
+    parser.add_argument('--verbose', '-v', action='count', default=0,
+                        help='Increase verbosity')
+    parser.add_argument('--quiet', '-q', action='count', default=0,
+                        help='Decrease verbosity')
+    parser.add_argument('--version', action='version', version='%(prog)s 0.0.0')
+    parser
