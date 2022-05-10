import weakref
+
+
+class Node():
+    # Create node class with a value, next, and prev attributes
+    def __init__(self, value):
+        self.value = value
+        self.next = None
+        self.prev = None
+
+
+class LinkedList():
+    # Create Linked List class with a head and tail attributes
+    def __init__(self):
+        self.head = None
+        self.tail = None
+        self.length = 0
+
+    def __len__(self):
+        return self.length
+
+    def append(self, value):
+        # add a node to end of the linked list
+        new_node = Node(value)
+        self.length += 1
+        if self.tail is None:
+            self.head = new_node
+            self.tail = self.head
+        else:
+            self.tail.next = new_node
+            new_node.prev = self.tail
+            self.tail = new_node
+
