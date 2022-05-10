import weakref
+from functools import wraps
+
+from django.db.models import Q
+from django.conf import settings
+from django.contrib.contenttypes.models import ContentType
+
+from mptt.exceptions import InvalidMove
+
+from .models import TaggedItem, Tag
+
+
+class TagRegistry:
+
+    def __init__(self):
+        self._registry = {}
+
+    def get(self, content_type, field_name):
+        return self._registry[content_type][field_name]
+
+    def register(self, content_type, field_name):
+        self._registry.setdefault(content_type, {})[field_name] = TagModel(content_type, field_name)
+
+
+class TagModel:
+
+    def __init__(self, content_type, field_name):
+        self.content_type = content_type
+        self.field_name = field_name
+
+    @property
+   
