fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def f():
	try: 1//0
	except ZeroDivisionError: pass

# Frame is on the stack during optimization
locals = { 'f': f, 'fn': fn, 'i': i }
globals = locals
optimize.make_code(fn.__code__, {}, {}, locals, globals, False)
	
# Frame is on the heap during execution, so we can't detect that i exists
with suppress_stderr(): test_support.run_unittest(KnownFailureTest(test_frame, fn.__code__, {}, globals, locals))

# But if i exists in a global scope, we detect it.
globals = { 'i': 0 }
locals = {}
optimize.make_code(fn.__code__, {}, {}, locals, globals, False)
with suppress_stderr(): test_support.run_unittest(KnownFailureTest(test_frame, fn.__code__, {}, globals, locals))

del locals


def test_compare(code, expected):
