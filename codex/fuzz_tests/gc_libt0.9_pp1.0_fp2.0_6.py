import gc, weakref, sys 
+
+class A:
+    def __init__(self,val):
+        self.val = val 
+    def __repr__(self):
+        return str(self.val) 
+
+a = A(10)
+d = weakref.WeakValueDictionary()
+d['primary'] = a 
+
+print(d['primary']) # Prints 10 
+del a               # Removes the one reference 
+gc.collect()        # Run garbage collection right away
+print(d['primary']) # KeyError: 'primary' 
+
+# del d # Prints "deleted!" 
+

