import gc, weakref
+
+class testobj(object):
+    pass
+
+if __name__ == '__main__':
+    t1 = testobj()
+    t2 = testobj()
+    t1.t = t2
+    t2.t = t1
+    wr1 = weakref.ref(t1)
+    wr2 = weakref.ref(t2)
+    wr1()
+    wr2()
+    t1.t = None
+    t2.t = None
+    print(wr1())
+    print(wr2())
+    gc.collect()
+    print(wr1())
+    print(wr2())
+    print(wr1() is wr2())

