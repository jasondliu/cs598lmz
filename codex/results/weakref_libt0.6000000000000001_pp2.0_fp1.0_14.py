import weakref
+
+class MyClass(object):
+    def __init__(self, name):
+        self.name = name
+    def __del__(self):
+        print('MyClass.__del__')
+
+obj = MyClass('obj1')
+r = weakref.ref(obj)
+print(r)
+print(r())
+
+obj2 = MyClass('obj2')
+r2 = weakref.ref(obj2)
+print(r2)
+print(r2())
+
+del obj
+print(r)
+print(r())
+
+del obj2
+print(r2)
+print(r2())

