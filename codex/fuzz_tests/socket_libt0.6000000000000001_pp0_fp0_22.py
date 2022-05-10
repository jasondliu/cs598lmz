import socket
+from time import sleep
+
+
+def get_args():
+    parser = argparse.ArgumentParser(description="Python ping")
+    parser.add_argument(
+        "-t", "--timeout", default=1, type=int, help="Timeout in seconds"
+    )
+    parser.add_argument(
+        "-H", "--address", help="The address to ping (default: %(default)s)", default="google.com"
+    )
+    return parser.parse_args()
+
+
+def main():
+    args = get_args()
+    timeout = args.timeout
+    address = args.address
+    while True:
+        try:
+            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+            s.settimeout(timeout)
+            s.connect((address, 80))
+            print(f"{address} is up")
+            s.close()
+        except socket.error as e:
+            print(f"{address}
