import weakref
+
+	__slots__ = safe_slots_required
+
+	def __init__(self, kwargs):
+		for k in safe_slots_required:
+			setattr(self, k, kwargs[k])
+
+	def safe_callback(self, callback, args=[], kwargs={}):
+		try:
+			callback(*args, **kwargs)
+		except Exception as e:
+			print "Exception in callback '" + str(callback) + "': " + str(e)
+
+	def msg_send(self, msg, args=[], kwargs={}, src=None):
+		if not src:
+			src = self.src
+		if src.remote:
+			self.remote.msg_send(msg, args, kwargs, src)
+		else:
+			self.msg_callback(msg, args, kwargs, src)
+
+	def msg_callback(self
