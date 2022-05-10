import weakref
+
+class Node:
+    def __init__(self,val):
+        self.val = val
+        self.next = None
+
+class LinkedList:
+    def __init__(self):
+        self.head = None
+        self.tail = None
+
+    def append(self,val):
+        node = Node(val)
+        if self.head is None:
+            self.head = node
+            self.tail = weakref.ref(node)
+        else:
+            self.tail().next = node
+            self.tail = weakref.ref(node)
+
+    def __iter__(self):
+        current = self.head
+        while current:
+            yield current.val
+            current = current.next
+
+    def __repr__(self):
+        return str(self.__dict__)
+
+
+def reverse_linked_list(linked_list):
+    prev = None
+    current = linked_list.head
+    while
