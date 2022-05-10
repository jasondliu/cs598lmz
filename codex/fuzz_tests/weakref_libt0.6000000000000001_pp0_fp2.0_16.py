import weakref
+
+
+class CountedObject:
+    num_instances = 0
+
+    def __init__(self):
+        self.__class__.num_instances += 1
+
+    def __del__(self):
+        self.__class__.num_instances -= 1
+
+
+def object_demo():
+    print('Making three objects...')
+    obj1 = CountedObject()
+    obj2 = CountedObject()
+    obj3 = CountedObject()
+    print('{0} instances'.format(CountedObject.num_instances))
+    del obj1
+    print('{0} instances'.format(CountedObject.num_instances))
+    del obj2, obj3
+    print('{0} instances'.format(CountedObject.num_instances))
+
+
+class MyClass:
+    def __init__(self, name):
+        self.name = name
+
+
+def weakref_demo():
+    obj = MyClass('
