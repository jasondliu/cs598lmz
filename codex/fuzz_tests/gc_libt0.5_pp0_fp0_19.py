import gc, weakref
+
+class Node:
+    __slots__ = ['value', 'parent', 'left', 'right']
+    def __init__(self, value=None, parent=None, left=None, right=None):
+        self.value = value
+        self.parent = parent
+        self.left = left
+        self.right = right
+
+class BinaryTree:
+    def __init__(self, root=None):
+        self.root = root
+
+    def __iter__(self):
+        if self.root is None:
+            return
+        stack = []
+        node = self.root
+        while stack or node:
+            if node:
+                stack.append(node)
+                node = node.left
+            else:
+                node = stack.pop()
+                yield node.value
+                node = node.right
+
+    def __contains__(self, value):
+        for node in self:
+            if node == value:
+                return True
+        return
