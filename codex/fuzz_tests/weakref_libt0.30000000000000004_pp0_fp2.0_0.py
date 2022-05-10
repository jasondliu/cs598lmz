import weakref
+
+
+class Node(object):
+    """
+    A node in a graph.
+    """
+
+    def __init__(self, data):
+        self.data = data
+        self.edges = []
+
+
+class Edge(object):
+    """
+    An edge in a graph.
+    """
+
+    def __init__(self, node_from, node_to):
+        self.node_from = node_from
+        self.node_to = node_to
+
+
+class Graph(object):
+    """
+    A graph.
+    """
+
+    def __init__(self, nodes=None, edges=None):
+        self.nodes = nodes or []
+        self.edges = edges or []
+        self._node_map = {}
+
+    def add_node(self, node):
+        """
+        Adds a Node to the graph.
+        """
+
+        self.nodes.append(node)

