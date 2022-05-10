import _struct
+
+class Node:
+    def __init__(self, data, left=None, right=None):
+        self.data = data
+        self.left = left
+        self.right = right
+
+def serialize(node, f):
+    if node == None:
+        f.write(_struct.pack("i", -1))
+        return
+
+    f.write(_struct.pack("i", node.data))
+    serialize(node.left, f)
+    serialize(node.right, f)
+
+def deserialize(f):
+    byte = f.read(4)
+    if byte == b"":
+        return None
+
+    value = _struct.unpack("i", byte)[0]
+    if value == -1:
+        return None
+
+    node = Node(value)
+    node.left = deserialize(f)
+    node.right = deserialize(f)
+    return node
+
+def test():
+   
