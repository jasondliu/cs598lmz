fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: segfault when __code__ is not a code object
import _testcapi
_testcapi.crash_no_current_frame(1)

# Issue #24091: segfault when __code__ is not a code object
import _testcapi
_testcapi.crash_no_current_frame(2)

# Issue #24091: segfault when __code__ is not a code object
import _testcapi
_testcapi.crash_no_current_frame(3)

# Issue #24091: segfault when __code__ is not a code object
import _testcapi
_testcapi.crash_no_current_frame(4)

# Issue #24091: segfault when __code__ is not a code object
import _testcapi
_testcapi.crash_no_current_frame(5)

# Issue #24091: segfault when __code__ is not a code object
import _
