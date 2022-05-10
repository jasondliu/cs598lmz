import weakref
+
+class A:
+    def __init__(self,value):
+        self.value = value
+    def __del__(self):
+        print('value has been deleted')
+
+
+a = A(8)
+print(a)       #<__main__.A object at 0x0253C758>
+d = weakref.weakref(a)
+print(d)       #<weakref at 0x02548090; to 'A' at 0x0253C758>
+print(d())     #<__main__.A object at 0x0253C758>
+del a
+print(d())     #None    value has been deleted
+
+
+
+import weakref
+
+class A:
+    def __init__(self,value):
+        self.value = value
+    def __del__(self):
+        print('value has been deleted')
+
+
+a = A(8)
+print(a)       #<__main__.A object at 0x0253
