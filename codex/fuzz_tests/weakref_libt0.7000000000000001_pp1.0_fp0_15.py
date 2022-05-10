import weakref
+
+
+class Node:
+    def __init__(self, value, left=None, right=None):
+        self.value = value
+        self.left = left
+        self.right = right
+
+    def __repr__(self):
+        return 'Node(%r, %r, %r)' % (self.value, self.left, self.right)
+
+
+def tree_to_nodes(root, parent=None):
+    if root is None:
+        return None
+    if hasattr(root, 'get'):
+        value = root.get('value', None)
+        left = root.get('left', None)
+        right = root.get('right', None)
+    else:
+        value = root[0]
+        left = root[1]
+        right = root[2]
+    left_node = tree_to_nodes(left, parent=value)
+    right_node = tree_to_nodes(right, parent=value)
+
