fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20897: segfault when __code__ is set to a non-code object
# with a co_code attribute.
import _testcapi
fn = lambda: None
fn.__code__ = _testcapi.make_capsule("foo")
fn()

# Issue #20897: segfault when __code__ is set to a non-code object
# with a co_code attribute.
import _testcapi
fn = lambda: None
fn.__code__ = _testcapi.make_capsule("foo")
fn()

# Issue #20897: segfault when __code__ is set to a non-code object
# with a co_code attribute.
import _testcapi
fn = lambda: None
fn.__code__ = _testcapi.make_capsule("foo")
fn()

# Issue #20897: segfault when __code__ is set to a non-code object
# with a co_code attribute.
import _testcapi
fn = lambda: None
