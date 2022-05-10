fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_sys_settrace
import sys

sys.settrace(lambda *args: None)

# test_sys_settrace_exception
import sys

sys.settrace(lambda *args: None)
1 / 0

# test_sys_settrace_recursion
import sys

sys.settrace(lambda *args: None)
sys.settrace(lambda *args: None)

# test_sys_settrace_return
import sys

sys.settrace(lambda *args: None)

# test_sys_settrace_return_exception
import sys

sys.settrace(lambda *args: None)
1 / 0

# test_sys_settrace_return_recursion
import sys

sys.settrace(lambda *args: None)
sys.settrace(lambda *args: None)

# test_sys_settrace_return_throw
import sys

sys.settrace(lambda *args: None)

# test_sys_settrace_throw
import sys

sys.settrace(
