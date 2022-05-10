import mmapi;
+
+def find_by_uuid(uuid):
+    """Find all objects with a given uuid."""
+    model = mmapi.PyModel();
+    mmapi.APIAddUUIDFilter(model, uuid);
+    api = mmapi.PyAssimpAPI();
+    api.ImportModel(model, None);
+    return model.GetObjects().values();
+
+def find_by_name(name):
+    """Find all objects with a given name."""
+    model = mmapi.PyModel();
+    mmapi.APIAddNameFilter(model, name);
+    api = mmapi.PyAssimpAPI();
+    api.ImportModel(model, None);
+    return model.GetObjects().values();
+
+def find_by_type(type):
+    """Find all objects of a given type."""
+    model = mmapi.PyModel();
+    mmapi.APIAddTypeFilter(model, type);
+    api = mmapi.PyAssimpAPI();
+   
