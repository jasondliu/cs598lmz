import select
+import sys
+import os
+import signal
+import psutil
+import time
+import subprocess
+import argparse
+import re
+
+
+def get_args():
+    parser = argparse.ArgumentParser(description='Process some integers.')
+    parser.add_argument('-p', '--port', type=int, help='port number')
+    parser.add_argument('-d', '--daemon', action='store_true', default=False, help='run in daemon mode')
+    parser.add_argument('--pidfile', default='/tmp/pyserver.pid', help='pid file')
+    parser.add_argument('--logfile', default='/tmp/pyserver.log', help='log file')
+    parser.add_argument('--log-level', default='DEBUG', help='log level')
+    return parser.parse_args()
+
+
+def get_logger(logfile, log_level):
+    logger = logging.getLogger()
+    logger.setLevel(log_
