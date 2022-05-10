fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #10: test_builtin_compile
# Issue #11: test_builtin_exec
# Issue #12: test_builtin_eval
# Issue #13: test_builtin_execfile
# Issue #14: test_builtin_file
# Issue #15: test_builtin_filter
# Issue #16: test_builtin_float
# Issue #17: test_builtin_frozenset
# Issue #18: test_builtin_hash
# Issue #19: test_builtin_hex
# Issue #20: test_builtin_id
# Issue #21: test_builtin_int
# Issue #22: test_builtin_intern
# Issue #23: test_builtin_iter
# Issue #24: test_builtin_len
# Issue #25: test_builtin_long
# Issue #26: test_builtin_map
# Issue #27: test_builtin_max
# Issue #28: test_builtin_min
# Issue #29: test_builtin_oct
# Issue #
