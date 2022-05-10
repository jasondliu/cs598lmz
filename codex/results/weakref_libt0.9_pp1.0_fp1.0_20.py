import weakref
+
+def timer(func):
+    def wrapper(*args, **kargs):
+        print("start timer")
+        start = time.time()
+        func(*args, **kargs)
+        end = time.time()
+        print("end timer:{}".format(end - start))
+    return wrapper
+
+def weak_method(func):
+    def wrapper(*args, **kargs):
+        arguments = inspect.getcallargs(func, *args, **kargs)
+        instance, method_name = None, None
+
+        for k, v in arguments.items():
+            if hasattr(v, "__self__"):
+                instance = v.__self__
+                method_name = v.__name__
+                break
+
+        if instance and method_name:
+            func(*args, **kargs)
+            print("Object has been destroyed?")
+            print(instance)
+        else:
+            print("no object")
+    return wrapper
+
+@timer

