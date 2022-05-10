import gc, weakref
+import sys
+
+class A:
+    def __init__(self):
+        self.a = "a"
+
+    def __del__(self):
+        print("del")
+
+def main():
+    a = A()
+    # 可以指定删除函数，手动调用
+    weakref.finalize(a, lambda x: print(x))
+    print(gc.get_referrers(a))
+    del a
+    print(gc.collect())
+    print(sys.getrefcount(a))
+    print(gc.get_referrers(a))
+
+
+if __name__ == "__main__":
+    main()

