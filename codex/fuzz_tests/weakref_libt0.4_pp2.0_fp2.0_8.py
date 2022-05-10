import weakref
from . import _coconut_sentinel as sentinel
from . import _coconut_tco as tco
from . import _coconut_igetitem as igetitem
from . import _coconut_base_pattern_func, _coconut_addpattern, _coconut_mark_as_match
_coconut_match_to = _coconut.match_to
_coconut_addpattern = _coconut_addpattern
def _coconut_pipe(x, f): return f(x)
def _coconut_starpipe(xs, f): return f(*xs)
def _coconut_backpipe(f, x): return f(x)
def _coconut_backstarpipe(f, xs): return f(*xs)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_minus(*args): return _coconut.operator.neg(*args) if len(args
