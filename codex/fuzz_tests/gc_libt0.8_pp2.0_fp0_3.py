import gc, weakref
+
+class A(object):
+	def __init__(self, value):
+		self.value = value
+	def __repr__(self):
+		return str(self.value)
+
+#a = A(10)
+#d = weakref.WeakValueDictionary()
+#d['primary'] = a
+#print (d['primary'])
+#del a
+#gc.collect()
+#print (d['primary'])
+
+#a = A(10)
+#d = weakref.WeakKeyDictionary()
+#d[a] = 'hello'
+#print (d[a])
+#del a
+#gc.collect()
+#print (d[a])
+
+a = A(10)
+d = weakref.WeakKeyDictionary()
+d[a] = 'hello'
+print (d[a])
+del a
+gc.collect()
+print (d[a])

