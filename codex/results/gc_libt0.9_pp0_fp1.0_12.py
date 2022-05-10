import gc, weakref
+from rpython.rtyper.memory.gctransform.test.test_boehm import AbstractGcIntegrationTest
+from rpython.translator.c.test.test_genc import compile
+from rpython.translator.c.gc import BoehmGCPolicy
+from rpython.rtyper.extregistry import ExtRegistryEntry
+from rpython.rlib.objectmodel import we_are_translated, compute_identity_hash
+from rpython.rlib.nonconst import NonConstant
+from rpython.rtyper.lltypesystem import rstr
+from rpython.rtyper.lltypesystem import lltype
+
+class CConfig:
+    _compilation_info_ = eci
+    GC_CAN_MOVE = True
+eci = ExternalCompilationInfo(post_include_bits=["""
+int ident_from_pyobj(PyObject* o) {
+    return PyObject_Hash(o);
+}
+"""], separate_module_sources=["""
+RPY_EX
