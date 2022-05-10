fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27071: Check that the repr of a code object with a generator
# doesn't crash.
import io
import traceback
with io.StringIO() as f:
    traceback.print_stack(file=f)
    s = f.getvalue()
    assert '<genexpr>' in s

# Issue #27071: Check that the repr of a code object with a generator
# doesn't crash.
import io
import traceback
with io.StringIO() as f:
    traceback.print_stack(file=f)
    s = f.getvalue()
    assert '<genexpr>' in s

# Issue #27071: Check that the repr of a code object with a generator
# doesn't crash.
import io
import traceback
with io.StringIO() as f:
    traceback.print_stack(file=f)
    s = f.getvalue()
    assert '<genexpr>' in s

# Issue #27071: Check that the repr of a code object with a generator
#
