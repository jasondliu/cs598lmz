import socket
+import logging
+import sys
+
+log = logging.getLogger("tcpclient")
+
+def _parse_args():
+    parser = argparse.ArgumentParser()
+    parser.add_argument("--host")
+    parser.add_argument("--port", type=int)
+    parser.add_argument("--debug", action="store_true")
+    return parser.parse_args()
+
+
+def _config_logging():
+    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
+    if args.debug:
+        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
+    else:
+        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
+
+
+def _main():
+    log.info("Server contacted")
+    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+
