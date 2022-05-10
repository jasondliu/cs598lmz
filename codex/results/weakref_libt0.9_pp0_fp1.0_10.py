import weakref
+
+
+class State(object):
+    def __init__(self, states={}):
+        self.state = {}
+        self.states = {}
+        self.states.update(states)
+
+    def set_state(self, name, data):
+        self.state[name] = data
+
+    def get_state(self, name):
+        if name in self.state:
+            return self.state[name]
+        elif name in self.states:
+            return self.states[name]()
+        else:
+            raise KeyError('State name {0} not exists'.format(name))
+
+    def del_state(self, name):
+        if name in self.state:
+            del self.state[name]
+
+
+class ClassState(State):
+    class StateMeta(type):
+        def __new__(mcs, name, bases, attr):
+            has_state = 'state' in attr
+            if not has_state:

