import select
+import sys
+import time
+
+from threading import Thread
+
+
+class Keyboard(Thread):
+    def __init__(self):
+        super(Keyboard, self).__init__()
+        self.running = False
+        self.key = None
+
+    def run(self):
+        self.running = True
+        while self.running:
+            time.sleep(0.05)
+            if self.key is not None:
+                continue
+            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
+                self.key = sys.stdin.read(1)
+
+    def stop(self):
+        self.running = False
+
+    def read(self):
+        key = self.key
+        self.key = None
+        return key
+
+
+def main():
+    keyboard = Keyboard()
+    keyboard.start()
+    try:
+        while True:
+            print(keyboard.read())
