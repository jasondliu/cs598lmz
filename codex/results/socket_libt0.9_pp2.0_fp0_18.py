import socket
+import json
+
+# server host
+host = 'localhost'
+# server port
+port = 5000
+
+# specify the right way to encode and decode the data in transfer
+coding = 'UTF-8'
+
+
+def main(argv):
+    # process the input arguments
+    if len(argv) < 2:
+        print("ERROR! too few arguments!")
+        print("Please follow the format: client.py [<mode> [<url>] ]")
+        sys.exit(0)
+    else:
+        mode = argv[0]
+        if mode == "evil":
+            if len(argv) < 3:
+                print("ERROR! too few arguments!")
+                print("Please follow the format: client.py evil [<url>] [<size>]")
+                sys.exit(0)
+        elif mode == "good":
+            # default number of files to download in good mode
+            if len(argv) == 3:
+                argv.append(10
