fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

import _testcapi

# Crash
_testcapi.call_invalid_code(fn)

# Segfault
_testcapi.call_invalid_code(gi)

# Segfault
_testcapi.call_invalid_code(gi.gi_code)
