fn = lambda: None
# Test fn.__code__.co_filename = '/home/user/myscript.py'
fn.__code__.co_filename = '/home/user/myscript.py'
fn.__code__.co_firstlineno = 10

traceback = _Traceback(fn)
</code>
or
<code>import sys

try:
    1/0
except ZeroDivisionError:
    _, _, traceback = sys.exc_info()
</code>

