import gc, weakref
+from contextlib import contextmanager
+
+import numpy as np
+
+import pytest
+
+import numba
+from numba import types
+from numba.core import config
+from numba.core.compiler import compile_isolated
+from numba.core.typing.templates import (AttributeTemplate, AbstractTemplate,
+                                         signature, Registry)
+from numba.tests.support import (TestCase, tag, MemoryLeakMixin,
+                                 CompilationCache, disable_leak_check)
+
+
+enable_pyobj_flags = numba.config.ENABLE_PYOBJECT
+
+
+def make_registry():
+    return Registry()
+
+
+def foo(x):
+    pass
+
+
+class TestAttributeTemplate(MemoryLeakMixin, TestCase):
+    """
+    Test attribute template
+    """
+
+    def setUp(self):
+        super(TestAttributeTemplate, self).setUp()
+        self.registry = make_
