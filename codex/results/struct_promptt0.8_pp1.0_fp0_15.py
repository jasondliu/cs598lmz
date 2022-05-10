import _struct
# Test _struct.Struct
s = _struct.Struct('3s3s')

import _testbuffer
# Test PyBUF_WRITABLE when processing a read-only buffer
no_rw = _testbuffer.readonly_copy()
no_rw.getbuffer()

# Test PyBUF_ND.
_testbuffer.test_PyBUF_ND()

import _testcapimodule
# Test PyCapsule_SetContext().
_testcapimodule.test()

# Test fixup_main_module
import _fixup_main_module
if getattr(sys, "_xoptions", None) is None:
    raise AssertionError("_xoptions was not set")
if getattr(sys, "_Py_HashRandomizationFlag", None) is None:
    raise AssertionError("_Py_HashRandomizationFlag was not set")

# Test PyPackage_GetInitModule
import _testimportmultiple

# Test PyGILState_Check
import _testgil
_testgil.test()

# Test PyMem_RawMalloc
import _testmem
_test
