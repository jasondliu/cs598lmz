import select
+
+
+class FileWatcher(object):
+
+    def __init__(self, *files):
+        self.files = files
+        self.poller = select.poll()
+
+    def add_file(self, path):
+        fd = open(path, 'r')
+        self.poller.register(fd, select.POLLIN)
+
+    def wait_for_events(self):
+        return self.poller.poll()
+
+    def do_something(self, fd):
+        print fd
+
+    def __call__(self):
+        for f in self.files:
+            self.add_file(f)
+        while True:
+            events = self.wait_for_events()
+            for fd, event in events:
+                self.do_something(fd)
+
+
+if __name__ == '__main__':
+    watch = FileWatcher('test1', 'test2')
+    watch()

