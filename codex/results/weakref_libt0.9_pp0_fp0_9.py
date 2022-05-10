import weakref
+
+
+class TopicRecord:
+    def __init__(self, ip, port, last_time):
+        self.ip = ip
+        self.port = port
+        self.last_time = last_time
+
+    def get_key(self):
+        return self.ip + " " + self.port
+
+
+class TopicInfoTracker:
+    def __init__(self):
+        self.lock = threading.Lock()
+        self.info_tracker = {}
+
+    def insert(self, topic_record):
+        self.lock.acquire()
+        try:
+            if self.info_tracker.setdefault(topic_record.get_key(), weakref.ref(topic_record)).__call__():
+                print("update time")
+            else:
+                print("new topic publisher")
+                self.info_tracker[topic_record.get_key()] = weakref.ref(topic_record)
+        finally:
+            self.lock.release()
