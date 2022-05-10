import gc, weakref
+
+class Observer(object):
+
+    def __init__(self, **kwargs):
+        # A dictionary of the object's attribute names and their values
+        self._observable_dict = dict(**kwargs)
+        self._observer_refs = []
+        for name, observable in self._observable_dict.items():
+            observable.attach(self, name)
+
+    def notify(self, observable, name):
+        # The observable calls this method when one of its observed attributes
+        # has changed state
+        print("{!r} has changed, name: {!r}".format(observable, name))
+
+    def __del__(self):
+        for name, observable in self._observable_dict.items():
+            observable.detach(self)
+
+
+class Observable(object):
+
+    def __init__(self, value=None, name=None):
+        self.value = value
+        self.name = name
+        self._ob
