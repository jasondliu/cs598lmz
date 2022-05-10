import gc, weakref
+
+# 弱引用
+
+# 如果一个对象只有弱引用，那么它的引用计数减为0的时候会被立即回收：
+a_set = {0, 1}
+wref = weakref.ref(a_set)
+print(wref)
+print(wref())
+a_set = {2, 3, 4}
+print(wref())
+print(wref() is None)
+
+# 弱引用只有在它引用的对象存在其他可达引用时才有效。
+# 如果它们之间没有其他可达引用，那
