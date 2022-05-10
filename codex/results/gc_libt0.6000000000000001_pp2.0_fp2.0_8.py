import gc, weakref
+
+class C:
+    def __init__(self, id):
+        self.id = id
+    def __repr__(self):
+        return 'C({})'.format(self.id)
+    def __del__(self):
+        print('del', self)
+
+if __name__ == '__main__':
+    o1 = C(1)
+    o2 = C(2)
+    o3 = C(3)
+    o1_wref = weakref.ref(o1)
+    o2_wref = weakref.ref(o2)
+    o3_wref = weakref.ref(o3)
+    print('initial:', o1_wref(), o2_wref(), o3_wref())
+    del o1, o2, o3
+    print('after del:', o1_wref(), o2_wref(), o3_wref())
+    gc.collect()
+    print('after collect:', o1_wref(),
