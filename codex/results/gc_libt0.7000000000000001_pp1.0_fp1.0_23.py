import gc, weakref
+
+# The weakref module provides a proxy for any object. The object does not 
+# need to be hashable. The reference is called a weak reference, and the 
+# proxy is called a weak reference object or, more simply, a weakref.
+# A weakref is a proxy to an object that does not increase its reference 
+# count. When the original object is no longer in use, it is automatically 
+# removed from a weakref table, and the weak reference object becomes 
+# invalid.
+class Cheese:
+    def __init__(self, kind):
+        self.kind = kind
+    
+    def __repr__(self):
+        return 'Cheese(%r)' % self.kind
+
+# To create a weakref, pass the object to the proxy constructor. 
+# The result is a weak reference to the object.
+# Create a few objects to demonstrate:
+stock = weakref.WeakValueDictionary()
+catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
+           Cheese('Brie'),
