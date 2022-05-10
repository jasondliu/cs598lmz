import gc, weakref
+
+class Foo():
+    def __init__(self, name):
+        self.name = name
+    def __del__(self):
+        print(self.name, 'has been deleted')
+
+obj = Foo('obj')
+obj1 = Foo('obj1')
+
+wref = weakref.ref(obj)
+wref1 = weakref.ref(obj1)
+
+print(wref, wref1)
+
+del obj
+gc.collect()
+
+print(wref, wref1)
+
+del obj1
+gc.collect()
+
+print(wref, wref1)
+
+
+class Greeting():
+    def sayhello(self, name):
+        print('Hello, ', name)
+
+    @classmethod
+    def saybye(cls, name):
+        print('Bye, ', name)
+
+    @staticmethod
+    def saywelcome(name):
+        print('Welcome, ', name)

