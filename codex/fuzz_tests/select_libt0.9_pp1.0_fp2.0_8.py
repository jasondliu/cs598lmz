import select
+
+import serial
+
+class Queue:
+    def __init__(self):
+        self.buffer = list()
+
+    def append(self, byte):
+        self.buffer.append(byte)
+
+    def put(self, byte):
+        self.buffer.append(byte)
+
+    def get(self):
+        return self.buffer.pop(0)
+
+    def len(self):
+        return len(self.buffer)
+
+def get_serial(tty, baudrate):
+    return serial.Serial(port=tty, baudrate=baudrate)
+
+def console_reader(stdin, queue):
+    for line in iter(stdin.readline, b''):
+        sys.stdout.write(line[:-1] + '\n')
+        queue.put(line)
+
+def main():
+    tty = sys.argv[1]
+    baudrate = sys.argv[2]
+
+   
