fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__class__(
    0, 0, 0, 0, b'', b'', (), (), '', '', 0, b''
)
fn.__globals__ = {
    '__builtins__': __builtins__,
    '__name__': __name__,
    '__doc__': None,
    '__package__': None,
}
sys.modules['time'] = fn
import time
fn.clock = time.clock
fn.sleep = time.sleep
fn.time = time.time
fn.perf_counter = time.perf_counter

sys.modules['builtins'] = __builtins__
import builtins
fn = lambda: None
fn.__code__ = fn.__code__.__class__(
    0, 0, 0, 0, b'', b'', (), (), '', '', 0, b''
)
fn.__globals__ = {
    '__builtins__': __builtins__,
    '__name__': __name__,
    '__doc__': None,

