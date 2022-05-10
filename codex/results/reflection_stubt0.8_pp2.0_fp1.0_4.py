fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# TypeError: 'code' attribute is not writable

# fn.__code__ = lambda x: 0
# fn.__code__ = 5
# fn.__code__ = b'abc'
```

```
# encoding: UTF-8
import sys
from test import support
from test.support.script_helper import assert_python_ok

# a user defined attribute is not accessible from C
def capture(*args):
    stdout, stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = StringIO(), StringIO()
    try:
        func(*args)
    except:
        sys.stdout.seek(0)
        sys.stderr.seek(0)
        print(sys.stdout.read())
        print(sys.stderr.read(), file=sys.__stderr__)
        raise

def test_trash():
    class X: pass
    x = X()
    x.__code__ = 1
    assert not hasattr(
