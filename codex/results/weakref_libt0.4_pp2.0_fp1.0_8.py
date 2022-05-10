import weakref
+
+import numpy as np
+
+from . import _core
+from . import _util
+
+
+class _Input(object):
+    def __init__(self, input_type):
+        self.input_type = input_type
+
+    def __repr__(self):
+        return "<%s %r>" % (self.__class__.__name__, self.input_type)
+
+
+class _Output(object):
+    def __init__(self, output_type):
+        self.output_type = output_type
+
+    def __repr__(self):
+        return "<%s %r>" % (self.__class__.__name__, self.output_type)
+
+
+class _Node(object):
+    def __init__(self, node_type):
+        self.node_type = node_type
+        self.inputs = []
+        self.outputs = []
+
+    def __repr__(self):
+       
