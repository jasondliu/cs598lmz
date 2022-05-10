import gc, weakref
+# from time import clock
+
+class Object(object):
+    pass
+
+class Graph(object):
+    def __init__(self, name):
+        self.name = name
+        self.edges = weakref.WeakKeyDictionary()
+
+    def __str__(self):
+        return '%s:%s' % (self.__class__.__name__, self.name)
+
+    __repr__ = __str__
+
+    def addEdge(self, edge):
+        self.edges[edge.to] = edge
+
+graph = Graph('root')
+
+last = graph
+nodes = [graph]
+
+for i in xrange(100000):
+    node = Object()
+    nodes.append(node)
+    last.addEdge(Object())
+
+# print clock()
+del nodes, last
+# print clock()
+
+while graph.edges:
+    gc.collect()
+
+# print clock()

