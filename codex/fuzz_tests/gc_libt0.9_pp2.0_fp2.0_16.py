import gc, weakref
+from cleanup import WeakCall, WeakCaller
+
+class Object(object):
+	def __del__(self):
+		print('deleting Object instance', self)
+
+def print_val(obj):
+	print('printing Object instance', obj)
+
+# call a bound callable
+
+obj1 = Object()
+print('creating a bound WeakCall instance:')
+weak_meth = WeakCall(obj1.__del__)
+print('dangling reference to object:')
+del obj1 # bound method won't survive object del
+print('calling bound function:')
+try:
+	weak_meth() # ValueError should be raised
+except ValueError:
+	print('weak_meth is dead!')
+del weak_meth # have to manually clean up
+
+# call an unbound callable
+
+print('creating an unbound WeakCall instance:')
+weak_func = WeakCall(print_val)
+obj2 = Object()
+print('call an unbound function
