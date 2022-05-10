fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #28982: Test that the repr of a code object contains the filename
# and first line number.
import sys
import inspect

def f(): pass
code = f.__code__
assert code.co_filename in repr(code)
assert str(code.co_firstlineno) in repr(code)

# Issue #28982: Test that the repr of a code object contains the filename
# and first line number.
import sys
import inspect

def f(): pass
code = f.__code__
assert code.co_filename in repr(code)
assert str(code.co_firstlineno) in repr(code)

# Issue #28982: Test that the repr of a code object contains the filename
# and first line number.
import sys
import inspect

def f(): pass
code = f.__code__
assert code.co_filename in repr(code)
assert str(code.co_firstlineno) in repr(code)

# Issue #28982: Test that the repr of a code object contains
