import gc, weakref
+
+
+class Event():
+
+	def __init__(self):
+
+		self.listeners = weakref.WeakKeyDictionary()
+
+
+	def add(self, listener):
+
+		self.listeners[listener] = 1
+
+
+	def remove(self, listener):
+
+		if listener in self.listeners.keys():
+			del self.listeners[listener]
+
+
+	def fire(self, *args, **kargs):
+
+		for listener in self.listeners.keys():
+			listener(*args, **kargs)
+
+
+	def clear(self):
+
+		self.listeners.clear()
+
+
+	def count(self):
+
+		return len(self.listeners)
+
+
+	if __name__ == '__main__':
+
+		class C:
+
+			def __init__(self):

