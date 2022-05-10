import weakref
+
+
+class User(ABCPlugin):
+    def __init__(self, plugin_manager, core, user_init_list, *args, **kwargs):
+        self.usernames = weakref.WeakValueDictionary()
+        user_init_list.append(self.__class__)
+
+    def __del__(self):
+        ...
+    # TODO: more

