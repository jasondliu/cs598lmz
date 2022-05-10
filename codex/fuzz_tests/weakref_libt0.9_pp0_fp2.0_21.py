import weakref
+
+__all__ = ['SingletonMeta']
+
+
+class SingletonMeta(type):
+    def __init__(self, *args, **kwargs):
+        self.__instance = None
+        super(SingletonMeta, self).__init__(*args, **kwargs)
+
+    def __call__(self, *args, **kwargs):
+        if self.__instance is None:
+            self.__instance = super(SingletonMeta, self).__call__(*args, **kwargs)
+
+            # Check if instance is not weakref proxy
+            # In this case instance is weakref.proxy(weakref.ref)
+            if not hasattr(self.__instance, '__func__'):
+                self.__instance = weakref.proxy(self.__instance)
+
+        return self.__instance

