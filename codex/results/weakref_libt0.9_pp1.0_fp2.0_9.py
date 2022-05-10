import weakref
+
+from . import event
+
+
+# pub-sub object
+
+# EventSource
+
+# EventConsumer
+
+# IDevice
+# IEvent
+# IMixer
+
+class IEventListener:
+  def __init__(self):
+    self.__init_events()
+    self.sources = weakref.WeakValueDictionary()
+    self.sinks = set()
+
+  def __init_events(self):
+    self.events = event.Event()
+    self.events.on()
+    self.events.defaults(sender=self)
+
+  def subscribe(self, source):
+    self.sources[source.id] = source
+    self.events.listen(source.events)
+
+  def unsubscribe(self, source):
+    self.events.unlisten(source.events)
+    del self.sources[source.id]
+
+  def unsubscribe_id(self, source_id):
+
