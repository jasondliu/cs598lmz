import weakref
+
+
+class ObjectFactory(object):
+    def __init__(self):
+        self._classes = {}
+        self._cache = {}
+
+    register = lambda s, cls: s._classes.setdefault(cls.__name__, cls)
+    get = lambda s, name, *a, **kw: weakref.proxy(s._classes.get(name, s._cache.setdefault(name, s._classes[name](*a, **kw))))
+    has = lambda s, name: name in s._classes
+
+
+class BaseObject(object):
+    def __init__(self, **kwargs):
+        for k, v in kwargs.items():
+            setattr(self, k, v)
+
+    def __repr__(self):
+        return "<%s %s>" % (self.__class__.__name__, {k: v for k, v in self.__dict__.items() if not k.startswith('_')})
+
+
+OF
