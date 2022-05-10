import weakref
+
+
+class Notifier:
+    def __init__(self):
+        self.observers = weakref.WeakSet()
+
+    def register(self, observer):
+        self.observers.add(observer)
+
+    def unregister(self, observer):
+        self.observers.discard(observer)
+
+    def notify(self, *args, **kwargs):
+        for observer in self.observers:
+            observer.notify(self, *args, **kwargs)
+
+
+class Observer:
+    def __init__(self, observer_callback):
+        self.observer_callback = observer_callback
+
+    def notify(self, notifier, *args, **kwargs):
+        if self.observer_callback:
+            self.observer_callback(notifier, *args, **kwargs)

