import mmap
+import os
+import re
+
+import pytest
+
+from .utils import get_target, PREFIX
+
+
+@pytest.fixture()
+def target(request):
+    return get_target(request)
+
+
+class TestStrided(object):
+
+    def test_strided_linear(self, target):
+
+        code = """
+void kernel1(int n, double* a) {
+    a[i*3+0] = 1;
+}
+        """
+        knl = lp.make_kernel(
+            "{[i]: 0<=i<n}",
+            "a[i*3+0] = 1;"
+            )
+        knl = lp.add_and_infer_dtypes(knl, {"a": np.float64})
+        knl = lp.split_iname(knl, "i", 3)
+        knl = lp.split_array_axis(knl, "a", 2, 3
