import gc, weakref
+
+class A:
+    def __del__(self):
+        print('obj A is destroyed')
+
+class B:
+    def __del__(self):
+        print('obj B is destroyed')
+
+a = A()
+b = B()
+
+# 创建弱引用对象
+c = weakref.ref(a)
+d = weakref.ref(b)
+
+print(c, d)
+print(c(), d())
+
+del a
+del b
+
+gc.collect()
+
+print(c(), d())
+print('-'*50)
+
+
+
+class C:
+    def __init__(self, x):
+        self.x = x
+
+    def __del__(self):
+        print('obj C is destroyed')
+
+    def getx(self):
+        return self.x
+
+c1 = C(10)
+c2 = C(
