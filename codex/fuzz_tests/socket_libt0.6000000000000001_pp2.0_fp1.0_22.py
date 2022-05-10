import socket
+import os
+from datetime import datetime
+
+
+def get_remote_machine_info():
+    remote_host = 'www.python.org'
+    try:
+        print("IP address: %s" % socket.gethostbyname(remote_host))
+    except socket.error as err_msg:
+        print("%s: %s" % (remote_host, err_msg))
+
+
+def main():
+    get_remote_machine_info()
+
+
+if __name__ == "__main__":
+    main()

