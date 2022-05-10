import gc, weakref
+
+a_set = {0,1}
+wref = weakref.ref(a_set)
+print(wref)
+print(wref())
+
+a_set = {2,3,4}
+print(wref())
+print(wref() is None)
+
+class Cheese:
+    def __init__(self, kind):
+        self.kind = kind
+
+    def __repr__(self):
+        return "Cheese(%r)"%self.kind
+
+stock = weakref.WeakValueDictionary()
+catalog = [Cheese("Red Leicester"), Cheese("Tilsit"), Cheese("Brie"), Cheese("Parmesan")]
+for cheese in catalog:
+    stock[cheese.kind] = cheese
+
+# 本循环仅检查元素的存在是否会被触发针对它的弱引用触发。

