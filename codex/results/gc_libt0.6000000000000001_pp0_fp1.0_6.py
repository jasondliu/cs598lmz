import gc, weakref
+
+
+def create_graph(node_count):
+    nodes = [Node(i) for i in range(node_count)]
+    for i in range(node_count):
+        for j in range(i):
+            nodes[i].children.append(nodes[j])
+            nodes[j].children.append(nodes[i])
+    return nodes
+
+
+def get_object_size(obj):
+    return sys.getsizeof(obj)
+
+
+class Node:
+    def __init__(self, name):
+        self.name = name
+        self.children = []
+
+    def __repr__(self):
+        return 'Node({!r})'.format(self.name)
+
+
+if __name__ == '__main__':
+    root = create_graph(50)
+    print(get_object_size(root))
+
+    ref_dict = {}
+    for node in root:
+        ref_dict[node.name
