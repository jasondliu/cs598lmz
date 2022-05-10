import weakref
+from . import _test_class
+
+
+@pytest.fixture
+def test_class():
+    return _test_class.TestClass()
+
+
+@pytest.fixture
+def wref():
+    return weakref.ref(_test_class.TestClass())
+
+
+@pytest.fixture
+def test_class_instance():
+    return _test_class.TestClass()
+
+
+@pytest.fixture
+def test_class_instance_with_name(test_class_instance):
+    test_class_instance.name = "test_class_instance"
+    return test_class_instance
+
+
+@pytest.fixture
+def test_class_instance_dead():
+    return weakref.ref(_test_class.TestClass())
+
+
+def test_dead_instance_should_raise_exception(test_class_instance_dead):
+    with pytest.raises(ReferenceError):
+        test_class_instance_dead
