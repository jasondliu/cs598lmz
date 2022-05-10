fn = lambda: None
# Test fn.__code__ is not None
_has_code = lambda fn: hasattr(fn, '__code__')
_is_lambda = lambda fn: _has_code(fn) and bool(fn.__code__.co_flags & 0x20)
_is_named_lambda = lambda fn: _is_lambda(fn) and bool(fn.__name__)
# Test fn.__closure__ is not None
_has_closure = lambda fn: hasattr(fn, '__closure__')
_is_anonymous = lambda fn: _is_lambda(fn) and not _has_closure(fn)
_is_named = lambda fn: not _is_anonymous(fn)
_is_closure = lambda fn: _has_closure(fn) and not _is_anonymous(fn)
_is_closure_fn = lambda fn: _has_closure(fn) and _has_code(fn)
_is_fn = lambda fn: _has_code(fn) and not (_is_lambda(fn))
# Test fn.__globals__ is not None
_has_globals = lambda
