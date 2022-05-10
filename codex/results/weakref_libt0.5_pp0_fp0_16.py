import weakref
+
+
+class CachedType(type):
+
+    def __init__(cls, *args, **kwargs):
+        super().__init__(*args, **kwargs)
+        cls._cache = weakref.WeakValueDictionary()
+
+    def __call__(cls, *args):
+        if args in cls._cache:
+            return cls._cache[args]
+        else:
+            obj = super().__call__(*args)
+            cls._cache[args] = obj
+            return obj
+
+
+class Spam(metaclass=CachedType):
+    def __init__(self, name):
+        print('Creating Spam({!r})'.format(name))
+        self.name = name
+
+
+a = Spam('Guido')
+b = Spam('Diana')
+c = Spam('Guido')
+
+print(a is b)
+print(a is c)

