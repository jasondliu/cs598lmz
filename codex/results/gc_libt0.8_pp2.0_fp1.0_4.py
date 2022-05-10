import gc, weakref, copy
+
+def _mk_printer(obj):
+	'''
+	Return a name of an object.
+	'''
+	return getattr(obj, 'name', None)
+
+class Order():
+	'''
+	An order object that keeps track of orders.
+	'''
+	# Keeps track of the order of all objects
+	# This is only purpose of this object
+	_names = weakref.WeakValueDictionary()
+
+	def __new__(cls, name=None, *a, **kw):
+		'''
+		Create new object
+		'''
+		if name in cls._names:
+			obj = cls._names[name]
+			obj._counter += 1
+			return obj
+		obj = object.__new__(cls, *a, **kw)
+		obj._name = name
+		cls._names[name] = obj
+		return obj
+
+	
