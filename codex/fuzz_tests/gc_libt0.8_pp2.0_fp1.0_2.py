import gc, weakref
+
+
+@pytest.fixture
+def DummyClass():
+	class DummyClass:
+		pass
+	return DummyClass
+
+
+@pytest.fixture
+def DummySubclass():
+	class DummySubclass(DummyClass):
+		def __init__(self):
+			self.dummy_var = "dummy_var_value"
+
+	return DummySubclass
+
+
+@pytest.fixture
+def dummy_obj(DummyClass):
+	dummy_obj = DummyClass()
+	dummy_obj.dummy_var = "dummy_var_value"
+	return dummy_obj
+
+
+@pytest.fixture
+def dummy_subobj(DummySubclass):
+	return DummySubclass()
+
+
+@pytest.fixture
+def dummy_obj_ref(dummy_obj):
+	return weakref.ref(dummy_obj)
+
+

