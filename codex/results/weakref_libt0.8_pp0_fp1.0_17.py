import weakref
+from collections import defaultdict
+
+class Graph():
+    def __init__(self, directed=False):
+        self.E = set()
+        self.V = set()
+        self.directed = directed
+        self.node_neighbors = defaultdict(set)
+        self.edge_properties = {}
+
+    def add_vertex(self, v):
+        self.V.add(v)
+
+    def add_edge(self, u, v, **property):
+        self.E.add((u, v))
+        self.node_neighbors[u].add(v)
+        if not self.directed:
+            self.node_neighbors[v].add(u)
+        self.edge_properties[(u, v)] = property
+
+    def add_edges(self, edges):
+        for u, v in edges:
+            self.add_edge(u, v)
+
+    def get_edge_property(self, u, v, property_
