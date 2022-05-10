import gc, weakref
+
+class Person(object):
+    def __init__(self, name):
+        self.name = name
+        self.friend = None
+        self.spouse = None
+
+    def __del__(self):
+        print ('Removing ', self.name)
+
+    def __repr__(self):
+        return 'Person(%s, %s, %s)'%(self.name, self.friend, self.spouse)
+
+    def __str__(self):
+        return self.name
+
+
+def test1():
+    p1 = Person('ramesh')
+    p2 = Person('shyam')
+    p1.friend = p2
+
+    p1.spouse = p2
+    p2.spouse = p1
+
+    del(p1)
+
+    gc.collect()
+    duration = 5
+    t_end = time.time() + duration
+    while time.time() < t_end:
+       
