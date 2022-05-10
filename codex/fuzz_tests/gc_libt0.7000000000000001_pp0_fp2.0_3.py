import gc, weakref
+
+
+def f2(x):
+    x.append(2)
+
+
+def f1():
+    a = []
+    f2(a)
+    print(a)
+
+
+def f3():
+    a = []
+    b = weakref.ref(a)
+    f2(a)
+    print(b())
+
+
+f1()
+f3()
+
+
+def f(a, b):
+    a += b
+
+
+x = 1
+y = 2
+f(x, y)
+print(x, y)
+
+a = [1, 2]
+b = [3, 4]
+f(a, b)
+print(a, b)
+
+t = (10, 20)
+u = (30, 40)
+f(t, u)
+print(t, u)
+
+
+def f4(a, b):
+    a = b
+
+

