import gc, weakref, inspect, types
+
+print 'fetch an object from outside the chain'
+outer = {"a": 1}
+
+def makeCycle():
+    inner = {"b": 2}
+    inner["a"] = outer
+    outer["b"] = inner
+    return inner
+
+print 'create cycle'
+
+cycle = makeCycle()
+
+class MyObj:
+    pass
+
+print 'create MyObj instance'
+
+obj = MyObj()
+
+print 'mark object as uncollectable'
+
+obj.cycle = cycle
+obj.x = cycle[0]
+
+print 'installing trace function'
+
+counters = []
+def callback(info):
+    counters.append(gc.get_count())
+
+gc.set_debug(gc.DEBUG_SAVEALL)
+gc.callbacks.append(callback)
+
+del outer
+del cycle
+
+print 'collecting...'
+
+gc.collect()
+
+print '
