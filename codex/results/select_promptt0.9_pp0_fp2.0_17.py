import select
# Test select.select
select.select([],[],[])
select.select([],[],[],1.0)
select.select([],[],[],1.0,0)

import mmap
# Test mmap.mmap
mmap.mmap(-1, 4096)
mmap.mmap(0, 4096)
mmap.mmap(1, 4096)

### --- Tests for specific code areas ---

# Test code area for "if expected != recv:" in _testcapimodule.py:
# See: http://bugs.python.org/issue4600
# Check that the bug is fixed.
import _testcapimodule
a1 = _testcapimodule.rgc.rgc('x')
a2 = _testcapimodule.rgc.rgc('x')
assert _testcapimodule.rgc_test_equal(a1, a2)
assert not _testcapimodule.rgc_test_equal(a1, None)

# Test code area for "cpdef inline struct foo s = ..." in _testcapimodule.py
a
