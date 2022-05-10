import weakref
+
+
+class MyClass(object):
+    def __init__(self, name):
+        self.name = name
+
+    def __repr__(self):
+        return 'MyClass({})'.format(self.name)
+
+
+def callback(reference):
+    """Invoked when referenced object is garbage collected"""
+    print('callback({!r})'.format(reference))
+
+
+def weak_callback(weakref_):
+    """Invoked when weak reference object is garbage collected"""
+    print('weak_callback({!r})'.format(weakref_))
+
+
+def main():
+    obj = MyClass('obj')
+    p = weakref.proxy(obj)
+    print('p:', p)
+
+    r = weakref.ref(obj, callback)
+    print('before:', r)
+    print('before:', obj)
+
+    del obj
+    print('after:', r)
+    print('after:', p)
+

