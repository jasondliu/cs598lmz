import gc, weakref
+
+
+class A(object):
+    def __init__(self, value):
+        self.value = value
+
+    def __repr__(self):
+        return str(self.value)
+
+
+a = A(10)
+d = weakref.WeakValueDictionary()
+d['primary'] = a
+print(d['primary'])
+del a
+gc.collect()
+print(d['primary'])
+
+
+class Cheese(object):
+    def __init__(self, kind):
+        self.kind = kind
+
+    def __repr__(self):
+        return 'Cheese(%r)' % self.kind
+
+
+stock = weakref.WeakValueDictionary()
+catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
+
+for cheese in catalog:
+    stock[cheese.kind] = cheese
+
+print(sorted(stock.keys()))

