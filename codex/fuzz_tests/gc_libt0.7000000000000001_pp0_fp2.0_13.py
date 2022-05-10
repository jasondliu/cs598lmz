import gc, weakref, operator
+
+
+class Dot:
+    """
+    Simple wrapper class for using refs.
+    """
+    def __init__(self, x, y):
+        self.x, self.y = x, y
+
+
+class Line:
+    """
+    Simple wrapper class for using refs.
+    """
+
+    def __init__(self, dot1, dot2):
+        self.dot1 = dot1
+        self.dot2 = dot2
+
+    def __repr__(self):
+        return 'Line({}, {})'.format(self.dot1, self.dot2)
+
+
+def test_weakref():
+    """
+    Test weak reference.
+    """
+    d1 = Dot(1, 2)
+    d2 = Dot(3, 4)
+    l = Line(d1, d2)
+    lref = weakref.ref(l)
+
+    print(l)
+    del l
+    g
