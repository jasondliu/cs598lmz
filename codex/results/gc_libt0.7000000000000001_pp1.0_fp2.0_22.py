import gc, weakref, threading
+
+class WeakMethod(object):
+	def __init__(self, f):
+		self.f = f.im_func
+		self.c = weakref.ref(f.im_self)
+	def __call__(self):
+		if self.c() is None:
+			return None
+		else:
+			return self.f.__get__(self.c())
+
+class WeakCallable(object):
+	def __init__(self, f):
+		try:
+			self.f = weakref.ref(f.im_func)
+			self.c = weakref.ref(f.im_self)
+		except AttributeError:
+			# not a bound method
+			self.f = weakref.ref(f)
+			self.c = None
+	def __call__(self):
+		if self.c is not None and self.c() is None:
+
