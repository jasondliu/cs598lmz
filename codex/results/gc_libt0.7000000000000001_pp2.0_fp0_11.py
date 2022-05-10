import gc, weakref
+from common import *
+
+class Class:
+	def __init__(self):
+		self.value = 10
+
+def test():
+	obj = Class()
+	gc.collect()
+	assert not gc.garbage
+	obj2 = weakref.proxy(obj)
+	assert obj.value == obj2.value
+	del obj
+	gc.collect()
+	try: obj2.value
+	except ReferenceError: pass
+	else: raise Exception

