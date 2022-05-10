import _struct
+
+f = open('./cat', 'r+b')
+for i in range(10):
+    print(_struct.unpack('b', f.read(1)))

